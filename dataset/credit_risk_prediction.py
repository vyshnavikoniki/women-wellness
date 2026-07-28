import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
)

import joblib

data = pd.read_csv("dataset/credit_data.csv")

print("\nDataset")
print(data.head())


# Debt-to-Income Ratio
data["Debt_Income_Ratio"] = data["Debt"] / data["Income"]

# Loan-to-Income Ratio
data["Loan_Income_Ratio"] = data["Loan_Amount"] / data["Income"]

print("\nDataset after Feature Engineering")
print(data.head())


X = data.drop("Creditworthy", axis=1)
y = data["Creditworthy"]

# -------------------------------------------------------
# Train-Test Split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# -------------------------------------------------------
# Feature Scaling
# -------------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------------------------------------
# Models
# -------------------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

best_model = None
best_accuracy = 0

print("\n================ MODEL RESULTS ================\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    probability = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, prediction)
    precision = precision_score(y_test, prediction)
    recall = recall_score(y_test, prediction)
    f1 = f1_score(y_test, prediction)
    roc = roc_auc_score(y_test, probability)

    print(name)
    print("-----------------------------")
    print("Accuracy :", round(accuracy,3))
    print("Precision:", round(precision,3))
    print("Recall   :", round(recall,3))
    print("F1 Score :", round(f1,3))
    print("ROC AUC  :", round(roc,3))
    print()

    print(classification_report(y_test, prediction))

    cm = confusion_matrix(y_test, prediction)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(name)
    plt.show()

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# -------------------------------------------------------
# Save Model
# -------------------------------------------------------

joblib.dump(best_model, "models/credit_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Best Model Saved Successfully!")

# -------------------------------------------------------
# Predict New Customer
# -------------------------------------------------------

print("\nEnter New Customer Details")

income = float(input("Income: "))
debt = float(input("Debt: "))
credit_history = int(input("Credit History (1=Good,0=Bad): "))
loan = float(input("Loan Amount: "))
age = int(input("Age: "))
payment = int(input("Payment History (1=Good,0=Bad): "))

debt_income = debt / income
loan_income = loan / income

new_data = np.array([[
    income,
    debt,
    credit_history,
    loan,
    age,
    payment,
    debt_income,
    loan_income
]])

new_data = scaler.transform(new_data)

prediction = best_model.predict(new_data)

if prediction[0] == 1:
    print("\nCredit Status: CREDITWORTHY")
else:
    print("\nCredit Status: NOT CREDITWORTHY")