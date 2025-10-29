from sklearn.model_selection import GridSearchCV

def perform_grid_search(estimator, param_grid, X_train, y_train, cv=5, scoring=None):
    """
    Perform grid search to find the best hyperparameters for a given estimator.

    Args:
        estimator: The machine learning model (estimator) to be optimized.
        param_grid: Dictionary with parameters names (str) as keys and lists of parameter settings to try as values.
        X_train: Training data features.
        y_train: Training data labels.
        cv: Number of cross-validation folds (default is 5).
        scoring: A string or callable to evaluate the predictions on the test set.

    Returns:
        best_estimator: The estimator with the best found parameters.
        best_params: The best parameter setting found on the hold out data.
        best_score: The best score achieved with the best parameters.
    """
    grid_search = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=cv, scoring=scoring)
    grid_search.fit(X_train, y_train)

    return grid_search.best_estimator_, grid_search.best_params_, grid_search.best_score_