# src/model_evaluation.py

import os
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def evaluate_model(model, X_test, y_test, model_name="Model"):
    """
    Evaluates trained model,
    prints metrics,
    saves confusion matrix and classification report.
    """

    print(f"\nEvaluating {model_name}...")

    # -----------------------------
    # 1. Predictions
    # -----------------------------
    y_pred = model.predict(X_test)

    # -----------------------------
    # 2. Accuracy
    # -----------------------------
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} Accuracy: {accuracy * 100:.2f}%")

    # -----------------------------
    # 3. Classification Report
    # -----------------------------
    report = classification_report(y_test, y_pred)

    print("\nClassification Report:\n")
    print(report)

    # Create reports folder if not exists
    os.makedirs("../reports", exist_ok=True)

    # Save classification report
    with open("../reports/classification_report.txt", "w") as f:
        f.write(report)

    print("Classification report saved to reports/ folder ✅")

    # -----------------------------
    # 4. Confusion Matrix
    # -----------------------------
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    # Ensure screenshots folder exists
    os.makedirs("../reports/screenshots", exist_ok=True)

    # Save confusion matrix image
    plt.savefig("../reports/screenshots/confusion_matrix.png")
    plt.close()

    print("Confusion matrix saved to reports/screenshots/ ✅")

    return accuracy
