# Will got this using chat GPT
# Here's the modified custom cross-entropy loss function with class weights incorporated:

import torch

class CustomCrossEntropyLoss(torch.nn.Module):
    def __init__(self):
        super(CustomCrossEntropyLoss, self).__init__()

    def forward(self, input, target):
        log_softmax_values = torch.log_softmax(input, dim=1)
        
        # Calculate class weights
        class_weights = torch.tensor([1.0 / count for count in torch.bincount(target)], device=input.device)
        
        # Weight the losses by class weights
        weighted_losses = -target * log_softmax_values * class_weights[target]
        
        return torch.mean(torch.sum(weighted_losses, dim=1))

  # In this modified implementation, class weights are calculated based on the inverse of the count of each class in the target labels. 
  # The class weights are then applied to the losses during the computation of the loss value.



  
  # You can use this custom loss function in your PyTorch models in the same way as before. Here's a usage example similar to the previous one:
import torch
import torch.nn as nn
import torch.optim as optim

# Example data
input_data = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)

# Example model
model = nn.Linear(5, 10)

# Example custom loss function with class weights
criterion = CustomCrossEntropyLoss()

# Example optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Forward pass
output = model(input_data)

# Calculate loss
loss = criterion(output, target)

# Backward pass
loss.backward()

# Update weights
optimizer.step()
