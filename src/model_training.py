# src/model_training.py

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from model_evaluation import evaluate_model
from data_preprocessing import load_and_preprocess


def train_models(data_path):

    print("\nLoading and preprocessing data...")
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess(data_path)

    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            class_weight='balanced'
        ),

        "Decision Tree": DecisionTreeClassifier(
            max_depth=10,
            class_weight='balanced',
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=150,
            max_depth=12,
            class_weight='balanced',
            random_state=42,
            n_jobs=-1
        )
    }

    best_model = None
    best_accuracy = 0

    print("\nTraining Models...\n")

    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)

        accuracy = evaluate_model(model, X_test, y_test, name)

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model

    print("\n-----------------------------------")
    print(f"Best Model Selected: {best_model}")
    print(f"Accuracy: {best_accuracy * 100:.2f}%")
    print("-----------------------------------\n")

    return best_model, scaler, X_test, y_test