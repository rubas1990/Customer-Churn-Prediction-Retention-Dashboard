# utilidades pequeñas: simulador de impacto financiero


def simulate_revenue_impact(mean_revenue_per_user: float, n_customers: int, churn_rate: float, reduction_pct: float):
"""Simula ahorro en ingresos si churn se reduce en `reduction_pct` (ej: 0.1 = 10%).


Args:
mean_revenue_per_user (float): ARPU mensual
n_customers (int): número de clientes
churn_rate (float): churn actual (0-1)
reduction_pct (float): proporción de reducción de churn esperada (0-1)


Returns:
dict: {"lost_revenue_current", "lost_revenue_new", "savings"}
"""
lost_current = mean_revenue_per_user * n_customers * churn_rate
churn_new = churn_rate * (1 - reduction_pct)
lost_new = mean_revenue_per_user * n_customers * churn_new
savings = lost_current - lost_new
return {
'lost_revenue_current': lost_current,
'lost_revenue_new': lost_new,
'savings': savings
}
