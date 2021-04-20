import matplotlib.pyplot as plt
import seaborn as sns


def distribution(df, feature):
    '''Prints a Seaborn distribution graph with KDE
    given a dataframe and selected feature
    '''
    fig, ax = plt.subplots(figsize=(10, 8))
    graph = sns.histplot(data=df, x=feature, kde=True, bins='auto')
    graph.set(title=f"{feature} distribution")
    plt.show()


def scatter_correlation(df, feature1, feature2='rating'):
    '''Prints a Seaborn scatter plot to visualize correlation,
    given a dataframe and at least one feature
    (default y value is rating)
    '''
    fig, ax = plt.subplots(figsize=(10, 8))
    graph = sns.scatterplot(data=df, x=feature1, y=feature2)
    graph.set(title=f"{feature1} vs {feature2}")
    plt.show()


def box_plot(df, feature1, feature2='step_count'):
    '''Prints a Seaborn box plot to visualize feature spread
    given a dataframe and at least one feature
    (default y is step count)
    '''
    fig, ax = plt.subplots(figsize=(10, 8))
    graph = sns.boxplot(data=df, x=feature1, y=feature2)
    graph.set(title=f"{feature1} vs {feature2}")
    plt.show()


def plot_resids(model, x_train, y_true):
    '''Predicts values and plots a residual plot,
    given a dataframe and two valid array/series
    inputs of x values and true y values
    '''
    if len(x_train) == len(y_true):
        preds = model.predict(x_train)
        resids = y_true - preds
        plt.scatter(preds, resids)
        plt.title(f"Plot of Residuals, Largest Residual: {max(abs(resids))}")
        plt.show()
    else:
        print("Input values must be of equal length.")
