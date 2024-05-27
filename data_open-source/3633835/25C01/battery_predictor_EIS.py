import torch
import torch.nn as nn


class BatteryPredictor(nn.Module):
    def __init__(self, input_len):
        super().__init__()
        activate_function = nn.Tanh()
        self.fc1 = nn.Sequential(
            nn.Linear(input_len, 64),
            activate_function,
        )
        self.fc2 = nn.Sequential(
            nn.Linear(64, 128),
            activate_function,
        )
        self.fc3 = nn.Sequential(
            nn.Linear(128, 256),
            activate_function,
        )
        self.fc4 = nn.Sequential(
            nn.Linear(256, 512),
            activate_function,
        )
        self.fc5 = nn.Sequential(
            nn.Linear(512, 256),
            activate_function,
        )
        self.fc6 = nn.Sequential(
            nn.Linear(256, 128),
            activate_function,
        )
        self.fc7 = nn.Sequential(
            nn.Linear(128, 64),
            activate_function,
        )
        self.fc8 = nn.Sequential(
            nn.Linear(64, 32),
            activate_function,
        )
        self.fc9 = nn.Sequential(
            nn.Linear(32, 16),
            activate_function,
        )
        self.out = nn.Sequential(
            nn.Linear(16, 1),
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