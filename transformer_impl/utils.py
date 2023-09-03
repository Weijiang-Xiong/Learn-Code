import copy 
import torch 
import torch.nn as nn 

def clones(module, N):
    "Produce N identical layers."
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])

def subsequent_mask(size):
    """Mask out subsequent positions.
    
        >>> torch.triu(torch.ones((1, 5, 5)), diagonal=1)==0   
        tensor([[[ True, False, False, False, False],
                 [ True,  True, False, False, False],
                 [ True,  True,  True, False, False],
                 [ True,  True,  True,  True, False],
                 [ True,  True,  True,  True,  True]]])
    
    """
    attn_shape = (1, size, size)
    subsequent_mask = torch.triu(torch.ones(attn_shape), diagonal=1).type(
        torch.uint8
    )
    return subsequent_mask == 0
