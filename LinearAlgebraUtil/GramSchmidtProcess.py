from .Vector import Vector
from .Matrix import Matrix
from .LinearSystem import rank


def gram_schmidt_process(basis):
    matrix = Matrix(basis)
    assert rank(matrix) == matrix.row_num()
    res = [basis[0]]
    for i in range(1, len(basis)):
        p = basis[i]
        for j in res:
            p -= basis[i].dot(j) / j.dot(j) * j
        res.append(p)
    return res


def qr(A: Matrix):
    assert A.row_num() == A.col_num()
    basis = gram_schmidt_process([A.col_vector(i) for i in range(A.col_num())])
    q = Matrix([i / i.norm() for i in basis]).T()
    r = q.T() * A
    return q, r
