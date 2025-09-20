import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

print("🚀 Starting training script...")

# Load dataset
data_path = r"C:\Users\jashm\Desktop\Preterm\baby_data.csv"
data = pd.read_csv(data_path)

print("\n✅ Dataset loaded successfully!")
print("First 5 rows:\n", data.head())
print("\nShape of dataset:", data.shape)

# Features and target (exclude Gender)
X = data[["Weight", "Length", "HeadCircumference"]]
y = data["GestationalAge"]

print("\n📊 Features (X):\n", X.head())
print("\n🎯 Target (y):\n", y.head())

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n✅ Data split done!")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("\n✅ Model training completed!")

# Evaluate
score = model.score(X_test, y_test)
print(f"\n📈 Model R^2 Score on test set: {score:.2f}")

# Save model
model_file = "baby_model.pkl"
with open(model_file, "wb") as f:
    pickle.dump(model, f)

print(f"\n💾 Model saved as {model_file}")

# Test prediction
sample = [[3.2, 50, 13]]  # Example: weight=3.2, length=50, HC=13
pred = model.predict(sample)
print(f"\n🤖 Predicted Gestational Age for sample {sample}: {pred[0]:.2f} weeks")
