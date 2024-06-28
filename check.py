import torch

if not torch.cuda.is_available():
    print("CUDA is not available. Please check your installation.")
else:
    print("CUDA is available. GPU count:", torch.cuda.device_count())
