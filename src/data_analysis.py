"""
data_analysis.py
----------------
Performs statistical summaries, correlation analysis, and regression modeling.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def correlation_summary(df):
    """Return correlation matrix for key numerical columns."""
    numeric_cols = df.select_dtypes("number")
    return numeric_cols.corr()

def regression_analysis(df):
    """Fit a linear regression model and return coefficients & R²."""
    X = df[["gdp_per_capita", "healthy_life_expectancy", "social_support", "freedom_to_make_life_choices"]]
    y = df["happiness_score"]

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)

    coef_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": model.coef_.round(3)
    }).sort_values(by="Coefficient", ascending=False)

    return coef_df, r2
