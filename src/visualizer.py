import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def distribution(df, feature): 
    fig, ax = plt.subplots(figsize = (10, 8))
    graph = sns.histplot(data = df, x = feature, kde = True, bins = 'auto')
    graph.set(title = f"{feature} distribution")
    plt.show()

def scatter_correlation(df, feature1, feature2 = 'rating'):
    fig, ax = plt.subplots(figsize = (10, 8))
    graph = sns.scatterplot(data = df, x = feature1, y = feature2)
    graph.set(title = f"{feature1} vs {feature2}")
    plt.show()

def box_plot(df, feature1, feature2 = 'step_count'):
    fig, ax = plt.subplots(figsize = (10,8))
    graph = sns.boxplot(data = df, x = feature1, y = feature2)
    graph.set(title = f"{feature1} vs {feature2}")
    plt.show()

def plot_resids(model, x_train, y_true):
    if (type(x_train) == np.ndarray or type(x_train) == pd.core.series.Series) and (type(y_true) == np.ndarray or type(y_true) == pd.core.series.Series):
        preds = model.predict(x_train)
        resids = y_true - preds
        plt.scatter(preds, resids)
        plt.title(f"Plot of Residuals, Largest Residual: {max(abs(resids))}")
        plt.show()
    else:
        print("Input values must be a series or array.")