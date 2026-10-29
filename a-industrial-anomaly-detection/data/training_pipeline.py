import torch
import torch.nn as nn
import mlflow
import mlflow.pytorch

from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split

torch.manual_seed(42)

X = torch.randn(1000, 3)

y = 2 * X[:, 0:1] - 3 * X[:, 1:2] + 0.5 * X[:, 2:3] + 1

X_train, X_val, y_train, y_val = train_test_split(
    X.numpy(), y.numpy(), test_size=0.2, random_state=42
)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
y_val = torch.tensor(y_val, dtype=torch.float32)

train_dataset = TensorDataset(X_train, y_train)
val_dataset = TensorDataset(X_val, y_val)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

model = nn.Sequential(nn.Linear(3, 16), nn.ReLU(), nn.Linear(16, 1))

loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

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

            train_loss_sum += loss.item() * len(batch_X)
            train_count += len(batch_X)

        train_loss = train_loss_sum / train_count

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

        mlflow.log_metrics(
            {"train_loss": train_loss, "val_loss": val_loss}, step=epoch + 1
        )

        print(
            f"Epoch {epoch + 1:02d} | "
            f"Train Loss: {train_loss:.6f} | "
            f"Val Loss: {val_loss:.6f}"
        )

    mlflow.pytorch.log_model(model, name="regression_model")

print("Training completed.")
