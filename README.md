# 💳 Online Payments Fraud Detection System

A Machine Learning based web application developed to detect fraudulent online payment transactions using classification models and a Flask web interface.

---

## 👩‍💻 Developed By

- Kartheeka Chevvakula
- Joshika
- Hima Sree
- Lavanya

Final Year B.Tech Project  
APSCHE Long Term VIP Program  

---

## 📌 Project Overview

The objective of this project is to build an intelligent fraud detection system that can identify fraudulent online transactions based on transaction details.

Multiple machine learning models were trained and evaluated.  
The best performing model was selected and deployed using Flask.

---

## 🧠 Models Implemented

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier (Selected Model)

### ✅ Best Model:
Random Forest Classifier  
Accuracy: **99.97%**

Model selection was based on:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📊 Features Used

- Transaction Type
- Step (Time)
- Amount
- Old Balance (Origin)
- New Balance (Origin)
- Old Balance (Destination)
- New Balance (Destination)

Target Variable:
- 0 → Not Fraud
- 1 → Fraud

---

## ⚙️ Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Flask
- HTML & CSS

---

## 📁 Project Structure
# 💳 Online Payments Fraud Detection System

A Machine Learning based web application developed to detect fraudulent online payment transactions using classification models and a Flask web interface.

---

## 👩‍💻 Developed By

- Kartheeka Chevvakula
- Joshika
- Hima Sree
- Lavanya

Final Year B.Tech Project  
APSCHE Long Term VIP Program  

---

## 📌 Project Overview

The objective of this project is to build an intelligent fraud detection system that can identify fraudulent online transactions based on transaction details.

Multiple machine learning models were trained and evaluated.  
The best performing model was selected and deployed using Flask.

---

## 🧠 Models Implemented

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier (Selected Model)

### ✅ Best Model:
Random Forest Classifier  
Accuracy: **99.97%**

Model selection was based on:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 📊 Features Used

- Transaction Type
- Step (Time)
- Amount
- Old Balance (Origin)
- New Balance (Origin)
- Old Balance (Destination)
- New Balance (Destination)

Target Variable:
- 0 → Not Fraud
- 1 → Fraud

---

## ⚙️ Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Flask
- HTML & CSS

---

## 📁 Project Structure
Online-Payments-Fraud-Detection/
│
├── flask/
│ ├── static/
│ ├── templates/
│ └── app.py
│
├── models/
│ ├── payments.pkl
│ └── scaler.pkl
│
├── notebooks/
│ └── eda_visualization.ipynb
│
├── reports/
│ ├── screenshots/
│ ├── classification_report.txt
│ └── project_report.pdf
│
├── src/
│ ├── data_preprocessing.py
│ ├── model_training.py
│ ├── model_evaluation.py
│ └── save_model.py
│
├── requirements.txt
└── README.md

---

## 🚀 How to Run the Project

### 1️⃣ Install Requirements
    pip install -r requirements.txt

### 2️⃣ Train and Save Model
    python save_model.py

### 3️⃣ Run Flask Application
    python app.py

    Open in browser:
    http://127.0.0.1:5000/

---

## 📈 Key Highlights

✔ Multiple model comparison  
✔ Automatic best model selection  
✔ Class imbalance handling  
✔ Confusion matrix visualization  
✔ Classification report generation  
✔ Flask web deployment  
✔ Real-time fraud prediction  

---

## 📜 License

This project is developed for academic purposes under the APSCHe Long Term VIP Program.