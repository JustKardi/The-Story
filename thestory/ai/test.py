import torch
import torch_directml

# Correct way to check for DirectML in 2026
if torch_directml.is_available():
    print("DirectML is available!")
    
    # Use the helper to get the correct device object (privateuseone:0)
    device = torch_directml.device()
    print("Device:", device)
    
    # Create tensors using the device object
    x = torch.randn(2, 2).to(device)
    print("Tensor on DirectML:\n", x)
else:
    print("DirectML backend not found!")
