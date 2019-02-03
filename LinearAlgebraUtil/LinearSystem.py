from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero
from ._global import is_equal


class LinearSystem:
    def __init__(self, A: Matrix, b: Vector or Matrix):
        assert A.row_num() == len(b), "Row numbers of A must equal the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        if isinstance(b, Vector):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(A.row_num())]
        if isinstance(b, Matrix):
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list()) for i in
                       range(A.row_num())]
        self.pivots = []

    def guass_jordan_elimination(self):
        self._forward()
        self._backward()
        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def _forward(self):
        i, k = 0, 0
        while i < self._m and k < self._n:
            # 看Ab[i][k]是否可以是主元
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            if is_zero(self.Ab[i][k]):
                k += 1
                continue
            self.Ab[i] = self.Ab[i] * 1 / self.Ab[i][k]
            for j in range(i + 1, self._m):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]
            self.pivots.append(k)
            i += 1
            k += 1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][k]

    def _max_row(self, i, k, n) -> int:
        m = (self.Ab[i][k], i)
        for j in range(i + 1, n):
            if abs(self.Ab[j][k]) > abs(m[0]):
                m = (self.Ab[j][k], j)
        return m[1]

    def get_matrix(self):
        return Matrix([i.underlying_list() for i in self.Ab])

    def fancy_print(self):
        print(self.get_matrix().col_vector(self._n))


def inv(A: Matrix):
    if A.row_num() != A.col_num():
        return None
    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    if not ls.guass_jordan_elimination():
        return None
    return Matrix([i.underlying_list()[n:] for i in ls.Ab])
