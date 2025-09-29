# -*- coding: utf-8 -*-
"""
data_processing.py
Funciones para carga y limpieza del dataset Telco Customer Churn.
"""


import pandas as pd
import numpy as np




def load_data(path: str) -> pd.DataFrame:
"""Carga el CSV desde `path` y retorna un DataFrame.


Args:
path (str): ruta al archivo CSV.


Returns:
pd.DataFrame: dataset cargado.
"""
# leer CSV
df = pd.read_csv(path)
return df




def clean_data(df: pd.DataFrame) -> pd.DataFrame:
"""Limpieza básica:
- convertir tipos
- imputar valores
- eliminar columnas irrelevantes


Args:
df (pd.DataFrame): DataFrame original


Returns:
pd.DataFrame: DataFrame limpio
"""
df = df.copy()


# eliminar customerID (identificador)
if 'customerID' in df.columns:
df.drop(columns=['customerID'], inplace=True)


# reemplazar espacios vacíos en TotalCharges por NaN y convertir a float
if 'TotalCharges' in df.columns:
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].replace(' ', np.nan))
# imputar con mediana
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)


# convertir SeniorCitizen a categoría
if 'SeniorCitizen' in df.columns:
df['SeniorCitizen'] = df['SeniorCitizen'].astype('category')


# transformar object -> category donde aplique
obj_cols = df.select_dtypes(include=['object']).columns.tolist()
for c in obj_cols:
df[c] = df[c].astype('category')


return df




if __name__ == '__main__':
# prueba rápida local
df = load_data('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print('Cargado:', df.shape)
dfc = clean_data(df)
print('Columnas después limpieza:', dfc.dtypes)
