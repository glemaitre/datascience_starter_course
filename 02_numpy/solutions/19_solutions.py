X = np.random.uniform(size=(5, 2))
print(X)
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_normalized = (X - X_mean) / X_std
print(X_normalized)
print('Mean and std. dev. after normalization:\n {} +- {}'.format(
    X_normalized.mean(axis=0), X_normalized.std(axis=0)))
