import torch
from torch import nn 
import matplotlib.pyplot as plt

tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]], dtype=torch.float32)

tensor_B = torch.tensor([[7, 10],
                         [8, 11], 
                         [9, 12]], dtype=torch.float32)
print(torch.matmul(tensor_A, tensor_B.T))