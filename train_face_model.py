import cv2
import numpy as np
import torch
import torch.nn as nn


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


# load saved model
model = FERModel()
model.load_state_dict(torch.load("models/face_model.pth"))
model.eval()


def detect_face_stress(image_path):

    img = cv2.imread(image_path, 0)

    img = cv2.resize(img, (48, 48))

    img = img / 255.0

    img = np.reshape(img, (1, 1, 48, 48))

    img_tensor = torch.tensor(img, dtype=torch.float32)

    with torch.no_grad():
        prediction = model(img_tensor)

    emotion = torch.argmax(prediction).item()

    # emotion to stress mapping
    if emotion in [0, 2, 4]:
        return 2      # High stress
    elif emotion == 6:
        return 1      # Medium stress
    else:
        return 0      # Low stress