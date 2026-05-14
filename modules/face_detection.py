import cv2
import numpy as np
import torch
import torch.nn as nn


class FERModel(nn.Module):
    def __init__(self):
        super(FERModel, self).__init__()

        self.network = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Flatten(),
            nn.Linear(64 * 10 * 10, 128),
            nn.ReLU(),
            nn.Linear(128, 7)
        )

    def forward(self, x):
        return self.network(x)


# load trained model
model = FERModel()
model.load_state_dict(torch.load("models/face_model.pth"))
model.eval()


def detect_face_stress(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return 0

    img = cv2.resize(img, (48, 48))

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=0)

    img_tensor = torch.tensor(img)

    with torch.no_grad():
        output = model(img_tensor)

    emotion = torch.argmax(output).item()

    # emotion → stress mapping
    if emotion in [0, 2, 4]:      # angry, fear, sad
        return 2                  # high
    elif emotion == 6:            # neutral
        return 1                  # medium
    else:
        return 0                  # low