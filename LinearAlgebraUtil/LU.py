from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero


def lu(matrix: Matrix) -> tuple:
    assert matrix.row_num() == matrix.col_num()
    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for i in range(n):
        if is_zero(A[i][i]):
            return None, None
        for j in range(i + 1, n):
            p = A[j][i] / A[i][i]
            A[j] = A[j] - p * A[i]
            L[j][i] = p
    U = [i.underlying_list() for i in A]
    return Matrix(L), Matrix(U)
