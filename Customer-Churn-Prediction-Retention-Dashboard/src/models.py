# -*- coding: utf-8 -*-
import argparse
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, f1_score, classification_report


from data_processing import load_data, clean_data
from features import prepare_features




def train_and_evaluate(path_csv: str, model_out: str = 'results/model.joblib') -> None:
"""Entrena modelos base y guarda el mejor según ROC-AUC.


Args:
path_csv (str): ruta al CSV
model_out (str): ruta para guardar el modelo final
"""
# 1) Cargar y limpiar
df = load_data(path_csv)
df = clean_data(df)


# 2) Features
X, y, encoder = prepare_features(df, target='Churn')


# 3) Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# 4) Entrenar dos modelos simples
models = {
'logreg': LogisticRegression(max_iter=1000),
'rf': RandomForestClassifier(n_estimators=100, random_state=42)
}


best_model = None
best_score = -np.inf
scores = {}


for name, model in models.items():
model.fit(X_train, y_train)
preds_proba = model.predict_proba(X_test)[:, 1]
preds = model.predict(X_test)
roc = roc_auc_score(y_test, preds_proba)
f1 = f1_score(y_test, preds)
scores[name] = {'roc_auc': roc, 'f1': f1}
print(f"{name}: ROC-AUC={roc:.4f}, F1={f1:.4f}")


if roc > best_score:
best_score = roc
best_model = model
best_name = name


# 5) Guardar mejor modelo y encoder
joblib.dump({'model': best_model, 'encoder': encoder}, model_out)
print(f"Mejor modelo: {best_name} guardado en {model_out}")


# 6) Reporte
preds = best_model.predict(X_test)
print('\nClassification report (mejor modelo):')
print(classification_report(y_test, preds))




if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--train', action='store_true', help='Entrenar modelo con dataset local')
parser.add_argument('--data', type=str, default='data/WA_Fn-UseC_-Telco-Customer-Churn.csv', help='Ruta al CSV')
parser.add_argument('--out', type=str, default='results/model.joblib', help='Ruta para guardar modelo')
args = parser.parse_args()


if args.train:
train_and_evaluate(args.data, args.out)
else:
print('Ejecuta con --train para entrenar')
