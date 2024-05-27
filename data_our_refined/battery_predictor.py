import torch
import torch.nn as nn


class BatteryPredictor(nn.Module):
    def __init__(self, input_len):
        super(BatteryPredictor, self).__init__()
        self.fc1 = nn.Sequential(
            nn.Linear(input_len, 32),
            nn.ReLU(),
        )
        self.fc2 = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
        )
        self.fc3 = nn.Sequential(
            nn.Linear(64, 72),
            nn.ReLU(),
        )
        self.fc4 = nn.Sequential(
            nn.Linear(72, 128),
            nn.ReLU(),
        )
        self.fc5 = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
        )
        self.fc6 = nn.Sequential(
            nn.Linear(64, 64),
            nn.ReLU(),
        )
        self.fc7 = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(),
        )
        self.fc8 = nn.Sequential(
            nn.Linear(32, 16),
            nn.ReLU(),
        )
        self.fc9 = nn.Sequential(
            nn.Linear(16, 8),
            nn.ReLU(),
        )
        self.out = nn.Sequential(
            nn.Linear(8, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.fc4(x)
        x = self.fc5(x)
        x = self.fc6(x)
        x = self.fc7(x)
        x = self.fc8(x)
        x = self.fc9(x)
        x = self.out(x)
        return x