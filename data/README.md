# 📊 Dataset Information  
## Online Payments Fraud Detection

---

## 📌 Dataset Source

The dataset used in this project is available on **Kaggle**:

👉 https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset

---

## 📂 Dataset Description

This dataset contains transaction-level information related to online payments.  
Each transaction record includes details such as:

- Transaction step  
- Transaction type  
- Amount  
- Sender balance before and after  
- Receiver balance before and after  
- Target label indicating fraud or not fraud

The dataset is used to train and evaluate machine learning models for detecting fraudulent transactions.

---

## 📈 Dataset Size

- **Original Size:** ~471 MB  
- **Type:** CSV file  
- **Number of Records:** Millions of rows  
- **Format:** `.csv`

Because of GitHub file size restrictions and repository performance, the full dataset is **not included** in this repository.

---

## 🧠 Features Used

The following columns are used for model training:

- `Step`  
- `Type`  
- `Amount`  
- `OldbalanceOrg`  
- `NewbalanceOrig`  
- `OldbalanceDest`  
- `NewbalanceDest`  
- `isFraud` *(target variable)*

---

## 🚧 Data Characteristics

- The dataset is highly imbalanced  
- Legitimate transactions are far more frequent than fraud  
- This imbalance requires careful handling during preprocessing and model training

---

## 📥 How to Use the Dataset

To work with the full dataset:

1. Go to the Kaggle dataset link above
2. Download the file
3. Save it inside this `data/` folder
4. Ensure the filename matches:
   Online_Payment_Fraud_Detection.csv
5. Run your training scripts, such as:

```bash
python src/data_preprocessing.py
python src/save_model.py

❗ Note
The dataset is intentionally not uploaded here due to large size and GitHub limitations.
Refer to the link above to obtain the dataset safely.
