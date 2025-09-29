# streamlit_app.py
# App simple que carga modelo y muestra métricas y simulador


import streamlit as st
import joblib
import pandas as pd
from src.data_processing import load_data, clean_data
from src.features import prepare_features
from src.utils import simulate_revenue_impact


st.set_page_config(page_title='Churn Dashboard', layout='wide')


st.title('Customer Churn — Dashboard')


uploaded = st.file_uploader('Carga aquí el CSV (Telco Customer Churn)', type='csv')


if uploaded is not None:
df = pd.read_csv(uploaded)
st.write('Muestra de datos:')
st.dataframe(df.head())


dfc = clean_data(df)
X, y, enc = prepare_features(dfc)


# cargar modelo si existe
try:
mdl = joblib.load('results/model.joblib')['model']
except Exception:
mdl = None


if mdl is not None:
proba = mdl.predict_proba(X)[:, 1]
dfc['churn_proba'] = proba
st.subheader('Top clientes con mayor probabilidad de churn')
st.dataframe(dfc.sort_values('churn_proba', ascending=False).head(20)[['churn_proba']])


st.subheader('Simulador financiero')
arpu = st.number_input('ARPU mensual (ej: 50)', value=50.0)
reduction = st.slider('Reducción de churn esperada (%)', 0, 100, 10)
churn_rate = (df['Churn'].map({'Yes':1,'No':0}).mean())
res = simulate_revenue_impact(arpu, df.shape[0], churn_rate, reduction/100)
st.metric('Ahorro mensual estimado', f"${res['savings']:,.2f}")


else:
st.info('Carga el dataset para activar el dashboard')
