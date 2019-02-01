from .Matrix import Matrix
from .Vector import Vector


class LinearSystem:
    def __init__(self, A: Matrix, b: Vector):
        assert A.row_num() == len(b), "Row numbers of A must equal the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n, "m must equal n"
        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(A.row_num())]

    def guass_jordan_elimination(self):
        self._forward()
        self._backward()

    def _forward(self):
        n = self._m
        for i in range(n):
            max_row = self._max_row(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            self.Ab[i] = self.Ab[i] * 1 / self.Ab[i][i]
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def _backward(self):
        n = self._m
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def _max_row(self, i, n) -> int:
        m = (self.Ab[i][i], i)
        for j in range(i + 1, n):
            if self.Ab[j][i] > m[0]:
                m = (self.Ab[j][i], j)
        return m[1]

    def get_matrix(self):
        return Matrix([i.underlying_list() for i in self.Ab])

    def fancy_print(self):
        print(self.get_matrix().col_vector(self._n))
