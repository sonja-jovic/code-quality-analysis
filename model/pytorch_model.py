import torch.nn as nn

class CodeQualityModel(nn.Module):

    def __init__(self):

        super().__init__()

        # Neural network architecture
        self.network = nn.Sequential(

            nn.Linear(4, 16),
            nn.ReLU(),

            nn.Linear(16, 8),
            nn.ReLU(),

            nn.Linear(8, 3)
        )

    def forward(self, x):

        return self.network(x)