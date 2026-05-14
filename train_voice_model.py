import torch
import torch.nn as nn
import os

os.makedirs("models", exist_ok=True)

class FERModel(nn.Module):
    def __init__(self):
        super(FERModel, self).__init__()

        self.network = nn.Sequential(
            nn.Conv2d(1, 32, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Flatten(),
            nn.Linear(6400, 128),
            nn.ReLU(),
            nn.Linear(128, 7)
        )

    def forward(self, x):
        return self.network(x)


model = FERModel()

# after training
torch.save(model.state_dict(), "models/face_model.pth")

print("Face model saved successfully")