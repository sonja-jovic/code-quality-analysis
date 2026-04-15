import pandas as pd
import torch

from sklearn.model_selection import train_test_split

from model.feature_extractor import extract_features
from model.pytorch_model import CodeQualityModel


df = pd.read_csv("data/dataset.csv")

label_map = {
    "bad": 0,
    "average": 1,
    "good": 2
}

X = []
y = []

for _, row in df.iterrows():

    code = row["code"].replace("\\n", "\n")

    features = extract_features(code)

    X.append(features)
    y.append(label_map[row["label"]])


X = torch.tensor(X).float()
y = torch.tensor(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = CodeQualityModel()

loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())


for epoch in range(50):

    preds = model(X_train)

    loss = loss_fn(preds, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print("Epoch:", epoch, "Loss:", loss.item())


torch.save(model.state_dict(), "trained_models/pytorch_model.pt")

print("Model saved.")