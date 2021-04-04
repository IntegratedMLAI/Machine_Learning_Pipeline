import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])
print()
print(type(X))
print(X.shape)
print()
X0 = X[:, 1].reshape(-1, 1)
print(X0.shape)
print(X0)
