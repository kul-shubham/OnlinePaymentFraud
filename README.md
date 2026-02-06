## End to End Machine Learning Project

# Online Payment Fraud Detection

This project uses Machine Learning to identify fraudulent online transactions. It features a complete pipeline from Exploratory Data Analysis (EDA) to a live web application for real-time prediction.

##  Project Structure
- `src/`: Source code including components and pipelines.
- `notebooks/`: Jupyter notebooks for EDA and model experiments.
- `artifacts/`: Stores `.csv` data, `.pkl` models.
- `app.py`: Flask web application.

##  Exploratory Data Analysis (Key Insights)
The EDA process uncovered several critical patterns in the dataset:
- **Fraud Distribution:** Fraudulent transactions are highly rare (approx. 0.13% of total data), indicating a severe class imbalance.
- **Transaction Types:** Fraud occurs exclusively in `TRANSFER` and `CASH_OUT` transaction types.


##  Getting Started
1. **Clone the repo:** `git clone <https://github.com/kul-shubham/OnlinePaymentFraud.git>`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Start the App:** `python app.py`

##  Tech Stack
- **Languages:** Python
- **Libraries:** Pandas, Seaborn, Matplotlib, Scikit-Learn
- **Deployment:** Flask
