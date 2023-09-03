from omegaconf import OmegaConf, ListConfig

# Create a configuration with a list
config_dict = {
    'model': {
        'name': 'resnet',
        'layers': ['conv1', 'conv2', 'conv3']
    }
}

# Load the configuration using OmegaConf
config = OmegaConf.create(config_dict)

# Access and modify the list using ListConfig
layers = config.model.layers
print(layers)  # Output: ['conv1', 'conv2', 'conv3']

# Append a new item to the list
layers.append('conv4')
print(layers)  # Output: ['conv1', 'conv2', 'conv3', 'conv4']

# Check if the list is an instance of ListConfig
if isinstance(layers, ListConfig):
    print("ListConfig")

# Convert ListConfig to a regular Python list
layers = list(layers)
print(layers)  # Output: ['conv1', 'conv2', 'conv3', 'conv4']

# Update the configuration
config.model.layers = layers

# Save the updated configuration
OmegaConf.save(config, 'config.yaml')