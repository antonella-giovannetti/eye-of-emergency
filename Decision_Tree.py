# custom decision tree class:

import numpy as np
import pandas as pd
from collections import Counter

class DecisionTree:

    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)

    def predict(self, X):
        return [self._predict(inputs) for inputs in X]

    def _predict(self, inputs):
        node = self.tree
        while node.children:
            if inputs[node.feature] < node.threshold:
                node = node.children[0]
            else:
                node = node.children[1]
        return node.prediction

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or n_labels == 1 or n_samples < 2:
            return Node(prediction=Counter(y).most_common(1)[0][0])

        # find the best split
        best_feature, best_threshold = None, None
        best_gini = 1.0
        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                y_left = y[X[:, feature] < threshold]
                y_right = y[X[:, feature] >= threshold]
                gini = (len(y_left) * self._gini(y_left) + len(y_right) * self._gini(y_right)) / n_samples
                if gini < best_gini:
                    best_feature = feature
                    best_threshold = threshold
                    best_gini = gini

        # grow the tree
        if best_gini < 1.0:
            left_idx = X[:, best_feature] < best_threshold
            X_left, y_left = X[left_idx], y[left_idx]
            X_right, y_right = X[~left_idx], y[~left_idx]
            children = [self._grow_tree(X_left, y_left, depth + 1),
                        self._grow_tree(X_right, y_right, depth + 1)]
            return Node(feature=best_feature, threshold=best_threshold, children=children)

        return Node(prediction=Counter(y).most_common(1)[0][0])

    def _gini(self, y):
        p = np.array(Counter(y).values()) / len(y)
        return 1.0 - np.sum(p ** 2)