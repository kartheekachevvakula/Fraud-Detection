# src/save_model.py

import os
import pickle

from model_training import train_models


def save_best_model(data_path):
    """
    Trains models, selects best one,
    and saves model + scaler to models folder.
    """

    print("\nStarting Model Training Pipeline...\n")

    # Train models and get best one
    best_model, scaler, X_test, y_test = train_models(data_path)

    # -----------------------------
    # Create models folder if not exists
    # -----------------------------
    os.makedirs("../models", exist_ok=True)

    # -----------------------------
    # Save Best Model
    # -----------------------------
    model_path = "../models/payments.pkl"
    scaler_path = "../models/scaler.pkl"

    with open(model_path, "wb") as f:
        pickle.dump(best_model, f)

    with open(scaler_path, "wb") as f:
        pickle.dump(scaler, f)

    print("\nModel saved at:", model_path)
    print("Scaler saved at:", scaler_path)
    print("\nTraining Pipeline Completed Successfully ✅")


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    save_best_model("../data/Online_Payment_Fraud_Detection.csv")
