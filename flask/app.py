from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('../models/payments.pkl', 'rb'))
scaler = pickle.load(open('../models/scaler.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/submit', methods=['POST'])
def submit():

    try:
        # Get values from form
        transaction_type = float(request.form['type'])
        step = float(request.form['step'])
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        # Feature order MUST match training
        features = np.array([[ 
            step,
            transaction_type,
            amount,
            oldbalanceOrg,
            newbalanceOrig,
            oldbalanceDest,
            newbalanceDest
        ]])

        # Scale input
        scaled_features = scaler.transform(features)

        # Predict class (0 or 1)
        prediction = model.predict(scaled_features)[0]

        # Get probabilities for both classes
        probabilities = model.predict_proba(scaled_features)[0]

        # Correct confidence score
        confidence = round(probabilities[prediction] * 100, 2)

        return render_template(
            'submit.html',
            prediction=prediction,
            confidence=confidence
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)