import numpy as np
import pandas as pd
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, prediction=None):
        self.feature = feature
        self.threshold = threshold
        self.prediction = prediction
        self.left = None
        self.right = None

class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    def fit(self, X, y):
        self.root = self._grow_tree(X, y)

    def predict(self, X):
        return [self._predict(inputs, self.root) for inputs in X]

    def _predict(self, inputs, node):
        while node.left and node.right:
            if inputs[node.feature] < node.threshold:
                node = node.left
            else:
                node = node.right
        return node.prediction

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))

        # Stopping criteria
        if (self.max_depth is not None and depth >= self.max_depth) or n_classes == 1 or n_samples < self.min_samples_split:
            return Node(prediction=self._most_common_label(y))

        # Find best split
        best_gini = 1.0
        best_feature = None
        best_threshold = None

        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                y_left = y[X[:, feature] < threshold]
                y_right = y[X[:, feature] >= threshold]
                gini = (len(y_left) * self._gini_impurity(y_left) + len(y_right) * self._gini_impurity(y_right)) / n_samples
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold

        # Create split
        if best_gini < 1.0:
            left_idx = X[:, best_feature] < best_threshold
            X_left, y_left = X[left_idx], y[left_idx]
            X_right, y_right = X[~left_idx], y[~left_idx]
            node = Node(feature=best_feature, threshold=best_threshold)
            node.left = self._grow_tree(X_left, y_left, depth + 1)
            node.right = self._grow_tree(X_right, y_right, depth + 1)
            return node

        return Node(prediction=self._most_common_label(y))

    def _gini_impurity(self, y):
        if len(y) == 0:
            return 0
        class_counts = np.bincount(y)
        class_probs = class_counts / len(y)
        return 1.0 - np.sum(class_probs ** 2)

    def _most_common_label(self, y):
        counter = Counter(y)
        if len(counter) == 0:
            return None
        return counter.most_common(1)[0][0]