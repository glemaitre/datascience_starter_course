X = np.random.randn(5, 2)
Y = np.random.randn(5, 2)
print(np.concatenate((X, Y), axis=0).shape)
print(np.concatenate((X, Y), axis=1).shape)
