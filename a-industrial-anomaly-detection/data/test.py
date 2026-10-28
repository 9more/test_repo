import torch
import torch.nn as nn

torch.manual_seed(42)

# Four training examples, each with two input features
X = torch.tensor(
    [
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
    ]
)

# Target is 1 when the two inputs differ, otherwise 0
y = torch.tensor(
    [
        [0.0],
        [1.0],
        [1.0],
        [0.0],
    ]
)

# Neural network with one hidden layer
model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
)

loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(2000):
    # Forward pass
    predictions = model(X)

    # Calculate loss across all four examples
    loss = loss_function(predictions, y)

    # Backpropagation and parameter updates
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 200 == 0:
        print(f"Epoch {epoch + 1}, " f"Loss: {loss.item():.6f}")

model.eval()

with torch.no_grad():
    final_predictions = model(X)

print("\nFinal predictions:")
print(final_predictions)
