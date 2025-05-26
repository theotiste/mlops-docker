import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Chargement et prétraitement
df = pd.read_csv("Cancer_Data_clean.csv")
X = df.drop(columns=["diagnosis"])
y = df["diagnosis"].map({"M": 1, "B": 0})

# Entraînement
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Sauvegarde
joblib.dump(model, "RandomForest.pkl")
print("✅ Modèle sauvegardé.")
