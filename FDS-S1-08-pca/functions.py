def standardize(df):
    return(df.apply(lambda x: (x - x.mean())/x.std(), axis=0))

def pca(X):
    Z = standardize(X)
    # Transpose the dataset, as pandas stores data in rows x features
    # and the covariance would be computed as the covariance of the
    # rows, but we are interested in the covariance of the features
    S = np.cov(Z.values.T) 
    P, lambdas = np.linalg.eig(S)
    return(P, lambdas)
