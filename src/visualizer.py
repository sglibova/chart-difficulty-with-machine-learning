import matplotlib.pyplot as plt
import seaborn as sns

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