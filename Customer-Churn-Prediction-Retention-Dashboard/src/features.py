# -*- coding: utf-8 -*-
"""
features.py
Feature engineering: encoding y creación de variables.
"""


import pandas as pd
from sklearn.preprocessing import OneHotEncoder




def prepare_features(df: pd.DataFrame, target: str = 'Churn') -> (pd.DataFrame, pd.Series, object):
"""Prepara variables para modelado:
- one-hot encode para variables categóricas
- devuelve X, y y el encoder para persistir


Args:
df (pd.DataFrame): DataFrame limpio
target (str): nombre de la variable objetivo


Returns:
X (pd.DataFrame), y (pd.Series), encoder (OneHotEncoder)
"""
df = df.copy()


# target binario
y = df[target].map({'Yes': 1, 'No': 0}) if df[target].dtype.name == 'category' or df[target].dtype == object else df[target]
X = df.drop(columns=[target])


# seleccionar categóricas y numéricas
cat_cols = X.select_dtypes(include=['category', 'object']).columns.tolist()
num_cols = X.select_dtypes(include=['number']).columns.tolist()


# OneHotEncoder para categóricas
ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
if cat_cols:
cat_trans = pd.DataFrame(ohe.fit_transform(X[cat_cols]),
columns=ohe.get_feature_names_out(cat_cols),
index=X.index)
X = pd.concat([X[num_cols], cat_trans], axis=1)
else:
X = X[num_cols]


return X, y, ohe




if __name__ == '__main__':
import pandas as pd
from data_processing import load_data, clean_data


df = load_data('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df = clean_data(df)
X, y, enc = prepare_features(df)
print('X shape:', X.shape)
