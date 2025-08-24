
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
from sklearn.ensemble import VotingClassifier

# Step 1: Generate synthetic stock market dataset
def generate_synthetic_data(samples=5000):
    np.random.seed(42)
    data = pd.DataFrame({
        "SMA_10": np.random.randn(samples) * 10 + 50,
        "SMA_50": np.random.randn(samples) * 10 + 52,
        "RSI": np.random.rand(samples) * 100,
        "MACD": np.random.randn(samples),
        "Volume": np.random.randint(1e5, 1e6, size=samples),
        "Volatility": np.abs(np.random.randn(samples)),
        "Price_Change_%": np.random.randn(samples) * 2
    })

    def label_row(row):
        if row["Price_Change_%"] > 1:
            return "Buy"
        elif row["Price_Change_%"] < -1:
            return "Sell"
        else:
            return "Hold"

    data["Signal"] = data.apply(label_row, axis=1)
    return data

df = generate_synthetic_data()
X = df.drop("Signal", axis=1)
y = df["Signal"].map({"Buy": 0, "Hold": 1, "Sell": 2})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

xgb = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42, n_estimators=50, max_depth=3)
svm = SVC(kernel='linear', probability=True, random_state=42)

ensemble = VotingClassifier(estimators=[
    ('xgb', xgb),
    ('svm', svm)
], voting='soft')

ensemble.fit(X_train_scaled, y_train)

y_pred = ensemble.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=["Buy", "Hold", "Sell"]))

df_test = X_test.copy()
df_test["Actual"] = y_test.map({0: "Buy", 1: "Hold", 2: "Sell"}).values
df_test["Predicted"] = pd.Series(y_pred).map({0: "Buy", 1: "Hold", 2: "Sell"}).values
df_test.to_csv("predictions_for_power_bi.csv", index=False)
