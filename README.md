# Customer-Churn-Prediction-Retention-Dashboard





**Description**: End-to-end project to predict churn in a subscription service and present a retention dashboard.


## Business problem
Companies lose revenue when customers leave. This project predicts customers at risk and simulates the financial impact of retention strategies.


## Dataset
Telco Customer Churn Dataset — download from Kaggle and place in `data/`.


## How to use
1. Clone this repo
2. Download the dataset and place it in `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`
3. Create a virtual environment and run `pip install -r requirements.txt`
4. Run `python src/models.py --train` to train the base model
5. Run `streamlit run dashboards/streamlit_app.py` to view the dashboard


## Structure
(see listing in the repo)


## Expected results
- Report with metrics (ROC-AUC, F1)
- Feature importance
- Interactive dashboard


## License
MIT

Translated with DeepL.com (free version)
