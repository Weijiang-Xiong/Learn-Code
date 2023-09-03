import copy 
import torch
import torch.nn as nn 
import torch.nn.functional as F

from utils import clones
from typing import Callable

class EncoderDecoder(nn.Module):
    """
    A standard Encoder-Decoder architecture. Base for this and many
    other models.
    """

    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator

    def forward(self, src, tgt, src_mask, tgt_mask):
        "Take in and process masked src and target sequences."
        return self.decode(self.encode(src, src_mask), src_mask, tgt, tgt_mask)

    def encode(self, src, src_mask):
        return self.encoder(self.src_embed(src), src_mask)

    def decode(self, memory, src_mask, tgt, tgt_mask):
        return self.decoder(self.tgt_embed(tgt), memory, src_mask, tgt_mask)
    
class Generator(nn.Module):
    "Define standard linear + softmax generation step."

    def __init__(self, d_model, vocab):
        super(Generator, self).__init__()
        self.proj = nn.Linear(d_model, vocab)

    def forward(self, x):
        return F.log_softmax(self.proj(x), dim=-1)

class LayerNorm(nn.Module):
    
    def __init__(self, size, eps=1e-6) -> None:
        super().__init__()
        self.alpha = nn.Parameter(torch.ones(size))
        self.beta = nn.Parameter(torch.zeros(size))
        self.eps = eps
        
    def forward(self, x:torch.Tensor):
        # x has shape N, T, C, reduce the channel dimension to get the mean and std
        # layernorm behaves the same in training and testing
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=False)
        return self.alpha * (x - mean) / (std + self.eps) + self.beta

class Encoder(nn.Module):
    
    """ Encoder will be a stack of encoder layers 
    """
    
    def __init__(self, layer, N):
        super(Encoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)
        
    def forward(self, x, mask):
        "Pass the input (and mask) through each layer in turn."
        for layer in self.layers:
            x = layer(x, mask)
        return self.norm(x)
    
class SublayerConnection(nn.Module):
    
    """ Residual connection and layer norm
    """
    
    def __init__(self, size, p, norm_first=False):
        # size is layernorm dimensions (excluding the batch dimension)
        # p is the dropout probability TODO why need dropout here?
        super().__init__()
        self.norm = LayerNorm(size)
        self.dropout = nn.Dropout(p)
        self.norm_first = norm_first
        
    def forward(self, x, sublayer_func:Callable):
        """       
        
        in the text blog, the text description is different from the code 
        use the procedure described in the text, which is also consistent with the paper 
        in pytorch implementation, this difference is handled by the norm_first flag
        https://pytorch.org/docs/stable/_modules/torch/nn/modules/transformer.html#TransformerEncoderLayer:~:text=x%20%3D%20src-,if%20self.norm_first%3A,-x%20%3D%20x

        Args:
            x (_type_): _description_
            sublayer_func (Callable): _description_

        Returns:
            _type_: _description_
        """
        if self.norm_first:
            return x + self.dropout(sublayer_func(self.norm(x)))
        else: 
            return self.norm(x + self.dropout(sublayer_func(x)))
    
    
class EncoderLayer(nn.Module):
    
    def __init__(self, size, p, attention, feed_forward):
        super().__init__()
        self.size = size
        self.self_attention = attention
        self.feed_forward = feed_forward
        self.att_sublayer = SublayerConnection(size, p)
        self.ff_sublayer = SublayerConnection(size, p)
    
    def forward(self, x, mask):

        x = self.att_sublayer(x, lambda x: self.self_attention(x, x, x, mask))
        x = self.ff_sublayer(x, self.feed_forward)
        
        return x 
    

class Decoder(nn.Module):
    
    "Generic N layer decoder with masking."

    def __init__(self, layer, N):
        super(Decoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)

    def forward(self, x, memory, src_mask, tgt_mask):
        for layer in self.layers:
            x = layer(x, memory, src_mask, tgt_mask)
        return self.norm(x)
    

class DecoderLayer(nn.Module):
    
    """
        A decoder layer consists of 1) query self-attention, 2) source-target attention and 3) feed-forward, each of them has a SublayerConnection structure
    """
    
    def __init__(self, size, self_attn, src_attn, feed_forward, dropout):
        super(DecoderLayer, self).__init__()
        self.size = size
        self.self_attn = self_attn
        self.src_attn = src_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 3)
        
    def forward(self, x, memory, src_mask, tgt_mask):
        "Follow Figure 1 (right) for connections."
        m = memory
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, tgt_mask))
        x = self.sublayer[1](x, lambda x: self.src_attn(x, m, m, src_mask))
        return self.sublayer[2](x, self.feed_forward)
    
