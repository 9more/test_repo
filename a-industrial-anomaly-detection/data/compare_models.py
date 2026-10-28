import torch
import torch.nn as nn
import mlflow
import mlflow.pytorch

from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split

# 1. Generate the same dataset for both models
torch.manual_seed(42)

X = torch.randn(1000, 3)

y = 2 * X[:, 0:1] - 3 * X[:, 1:2] + 0.5 * X[:, 2:3] + 1

# 2. Create a fixed train/validation split
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


# 3. Define the two architectures
def create_model(model_type):
    if model_type == "linear":
        return nn.Linear(3, 1)

    elif model_type == "hidden_layer":
        return nn.Sequential(nn.Linear(3, 16), nn.ReLU(), nn.Linear(16, 1))

    raise ValueError("Unknown model type")


# 4. Count trainable parameters
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


# 5. Training and validation function
def train_and_evaluate(model, epochs=50):
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(epochs):
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

        # Evaluate without updating parameters
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

    return train_loss, val_loss


# 6. Compare models using separate MLflow runs
mlflow.set_experiment("regression-model-comparison")

for model_type in ["linear", "hidden_layer"]:
    # Reset the seed for reproducible model initialisation
    torch.manual_seed(42)

    model = create_model(model_type)
    num_parameters = count_parameters(model)

    with mlflow.start_run(run_name=model_type):
        mlflow.log_params(
            {
                "model_type": model_type,
                "learning_rate": 0.01,
                "batch_size": 32,
                "epochs": 50,
                "num_parameters": num_parameters,
            }
        )

        final_train_loss, final_val_loss = train_and_evaluate(model, epochs=50)

        mlflow.log_metrics(
            {"final_train_loss": final_train_loss, "final_val_loss": final_val_loss}
        )

        mlflow.pytorch.log_model(
            model,
            name="model",
            serialization_format="pickle",
            input_example=torch.randn(1, 3),
        )
        print(
            f"{model_type} | "
            f"Parameters: {num_parameters} | "
            f"Train loss: {final_train_loss:.8f} | "
            f"Validation loss: {final_val_loss:.8f}"
        )

print("Model comparison completed.")
