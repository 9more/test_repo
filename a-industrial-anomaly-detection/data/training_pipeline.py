import torch
import torch.nn as nn
import mlflow
import mlflow.pytorch

from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split

# 1. Reproducibility
torch.manual_seed(42)

# 2. Generate synthetic data
X = torch.randn(1000, 3)

# Define a target with a learnable relationship to X
y = 2 * X[:, 0:1] - 3 * X[:, 1:2] + 0.5 * X[:, 2:3] + 1

# 3. Split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X.numpy(), y.numpy(), test_size=0.2, random_state=42
)

# Convert arrays back to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
y_val = torch.tensor(y_val, dtype=torch.float32)

# 4. Create datasets and mini-batch loaders
train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# 5. Define the neural network
model = nn.Sequential(nn.Linear(3, 16), nn.ReLU(), nn.Linear(16, 1))

# 6. Define loss and optimiser
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 7. Configure MLflow
mlflow.set_experiment("industrial-anomaly-learning")

with mlflow.start_run(run_name="baseline-regression"):
    mlflow.log_params(
        {
            "learning_rate": 0.01,
            "batch_size": 32,
            "epochs": 30,
            "hidden_units": 16,
            "optimizer": "Adam",
        }
    )

    # 8. Training loop
    for epoch in range(30):
        model.train()
        train_loss_sum = 0.0
        train_count = 0

        for batch_X, batch_y in train_loader:
            predictions = model(batch_X)
            loss = loss_function(predictions, batch_y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Accumulate error across examples
            train_loss_sum += loss.item() * len(batch_X)
            train_count += len(batch_X)

        train_loss = train_loss_sum / train_count

        # 9. Validation: no parameter updates
        model.eval()
        val_loss_sum = 0.0
        val_count = 0

        with torch.no_grad():
            for batch_X, batch_y in val_loader:
                predictions = model(batch_X)
                loss = loss_function(predictions, batch_y)

                val_loss_sum += loss.item() * len(batch_X)
                val_count += len(batch_X)

        val_loss = val_loss_sum / val_count

        # 10. Log metrics to MLflow
        mlflow.log_metrics(
            {"train_loss": train_loss, "val_loss": val_loss}, step=epoch + 1
        )

        print(
            f"Epoch {epoch + 1:02d} | "
            f"Train Loss: {train_loss:.6f} | "
            f"Val Loss: {val_loss:.6f}"
        )

    # 11. Save the trained model as an MLflow artefact
    mlflow.pytorch.log_model(model, name="regression_model")

print("Training completed.")
