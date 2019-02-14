import numpy as np


def diagonalize(A: np.ndarray):
    assert A.ndim == 2
    assert A.shape[0] == A.shape[1]
    lambdas, P = np.linalg.eig(A)
    assert np.linalg.matrix_rank(P) == P.shape[0]
    return P, np.identity(A.shape[0]) * lambdas, np.linalg.inv(P)
