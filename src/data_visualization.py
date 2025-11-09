"""
data_visualization.py
---------------------
Handles plotting of happiness relationships, heatmaps, and model visualizations.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df, save_path="../assets/happiness_correlation_heatmap.png"):
    plt.figure(figsize=(7, 5), dpi=120)
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Between Happiness and Key Factors", fontsize=11, weight="bold")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches="tight", transparent=True)
    plt.close()

def plot_regression_coeffs(coef_df, save_path="../assets/happiness_regression_coeffs.png"):
    plt.figure(figsize=(6, 4), dpi=120)
    sns.barplot(data=coef_df, x="Coefficient", y="Feature", palette="crest")
    plt.title("Feature Impact on Happiness (Linear Regression)", fontsize=11, weight="bold")
    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches="tight", transparent=True)
    plt.close()
