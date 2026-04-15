import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from model.feature_extractor import extract_features
from model.tensorflow_model import build_tf_model

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


X = np.array(X)
y = np.array(y)

model = build_tf_model()

model.fit(X, y, epochs=50)

model.save("trained_models/tensorflow_model.keras")

print("TensorFlow model saved.")