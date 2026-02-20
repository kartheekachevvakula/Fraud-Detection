import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_and_preprocess(data_path, sample_size=200000):

    print("Loading dataset...")
    df = pd.read_csv(data_path)

    print("Original Dataset Shape:", df.shape)

    # Reduce dataset size
    if sample_size and sample_size < len(df):
        df = df.sample(n=sample_size, random_state=42)
        print("Sampled Dataset Shape:", df.shape)

    # Encode transaction type
    df['type'] = df['type'].astype('category').cat.codes

    # Select features (WITH TYPE)
    selected_features = [
        'step',
        'type',
        'amount',
        'oldbalanceOrg',
        'newbalanceOrig',
        'oldbalanceDest',
        'newbalanceDest'
    ]

    X = df[selected_features]
    y = df['isFraud']

    print("Final Features Used:", X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Preprocessing Completed Successfully ✅")

    return X_train, X_test, y_train, y_test, scaler