import torch

print(f"PyTorch version {torch.__version__}")

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)

# Perform a basic operation

squared_tensor = tensor ** 2

# Print the original and squared tensor
print("Original Tensor:", tensor)
print("Squared  Tensor:", squared_tensor)

# Check GPU availibility
if torch.cuda.is_available():
    print("CUDA is available! Using GPU.")
    device = torch.device("cuda")
    tensor_gpu = tensor.to(device)
    print("Tensor on GPU:", tensor_gpu)
else:
    print("CUDA is not availible. Using CPU.")
