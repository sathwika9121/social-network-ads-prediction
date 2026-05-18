# Step 1: Import Libraries
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Load Dataset
df = pd.read_csv("Social_Network_Ads.csv")

print("Dataset Loaded Successfully ✅")
print(df.head())

# Step 3: Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Drop Unwanted Column
if "User ID" in df.columns:
    df = df.drop("User ID", axis=1)

# Step 5: Convert Gender Column
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

# Step 6: Select Features and Target
X = df[["Gender", "Age", "EstimatedSalary"]]
y = df["Purchased"]

# Step 7: Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 8: Feature Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 9: Train Logistic Regression Model
model = LogisticRegression()

model.fit(X_train_scaled, y_train)

# Step 10: Predict on Test Data
y_pred = model.predict(X_test_scaled)

# Step 11: Model Evaluation
print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 12: Save Files
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")

print("\n✅ model.pkl saved")
print("✅ scaler.pkl saved")
print("✅ columns.pkl saved")