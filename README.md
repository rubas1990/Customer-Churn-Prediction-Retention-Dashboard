Customer Churn Prediction & Retention Dashboard
🚀 Project Overview

This repository contains a full end-to-end data science project focused on predicting customer churn for a subscription-based business and delivering actionable insights through an interactive retention dashboard.

The project demonstrates expertise in the complete data science lifecycle: data cleaning, exploratory analysis, feature engineering, machine learning modeling, evaluation, and deployment-ready dashboards. It highlights the ability to turn business problems into data-driven solutions, a critical skill for tech leaders like Google, Meta, or Amazon.

🎯 Business Problem

Customer churn is a major source of revenue loss. Identifying at-risk customers allows companies to implement proactive retention strategies, optimize marketing campaigns, and reduce financial impact.

This project provides:

Churn Prediction: Identifies customers at high risk of leaving.

Financial Simulation: Estimates the impact of retention campaigns.

Interactive Dashboard: Tracks predictions, metrics, and insights in real time.

📊 Dataset

Telco Customer Churn Dataset (available on Kaggle).

Save the CSV in the data/ folder:

data/WA_Fn-UseC_-Telco-Customer-Churn.csv


The dataset includes: customer demographics, account details, service usage patterns, and contract information.

🔧 Key Skills Demonstrated

Data Preprocessing: Handling missing values, encoding categorical variables, feature scaling.

Exploratory Data Analysis: Statistical summaries, correlation analysis, and visualization to identify churn drivers.

Machine Learning: Logistic Regression, Random Forest, Gradient Boosting.

Model Evaluation: ROC-AUC, F1 score, confusion matrix, and feature importance analysis.

Dashboarding: Interactive Streamlit dashboard to visualize predictions, metrics, and retention scenarios.

End-to-End Pipeline: From raw data to actionable insights.

⚡ How to Use

Clone the repository:

git clone https://github.com/yourusername/Customer-Churn-Prediction-Retention-Dashboard.git


Place the dataset in data/.

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt


Train the predictive model:

python src/models.py --train


Launch the dashboard:

streamlit run dashboards/streamlit_app.py

📂 Project Structure
├── data/                  # Raw datasets
├── src/                   # Preprocessing, modeling, and evaluation scripts
├── dashboards/            # Streamlit dashboard
├── requirements.txt       # Dependencies
├── README.md              # Project documentation

📈 Expected Results

Trained models with metrics (ROC-AUC, F1 score).

Insights into the most important features driving churn.

Interactive dashboard showing predictions, retention strategies, and KPIs.

💡 Impact & Value

This project demonstrates the ability to:

Translate business challenges into data-driven solutions.

Apply end-to-end machine learning workflows with real datasets.

Communicate insights effectively through visualization and dashboards.

It showcases technical skills and business impact, making it highly relevant for tech companies focused on customer retention and analytics.

📝 License

MIT
