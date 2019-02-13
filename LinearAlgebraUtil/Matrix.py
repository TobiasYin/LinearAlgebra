from .Vector import Vector


class Matrix(object):
    def __init__(self, list2d: list):
        length = len(list2d[0])
        for i in list2d:
            assert type(i) == list or isinstance(i, Vector)
            assert len(i) == length
            for j in i:
                assert type(j) == int or type(j) == float
            if isinstance(list2d[0], list):
                self._values = [row[:] for row in list2d]
            elif isinstance(list2d[0], Vector):
                self._values = [row.underlying_list() for row in list2d]

    def size(self):
        s, z = self.shape()
        return s * z

    def shape(self):
        return len(self._values), len(self._values[0])

    def row_num(self):
        return self.shape()[0]

    def row_vector(self, index) -> Vector:
        return Vector(self._values[index])

    def col_vector(self, index) -> Vector:
        return Vector([i[index] for i in self._values])

    def dot(self, another):
        return self * another

    def T(self):
        return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])

    __len__ = row_num

    def __getitem__(self, position: tuple):
        r, c = position
        return self._values[r][c]

    def col_num(self):
        return self.shape()[1]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    def __str__(self):
        return "\n".join("\t".join(str(i) for i in j) for j in self._values)

    def __iter__(self):
        return self._values.__iter__()

    def __add__(self, other):
        assert self.shape() == other.shape(), "Error in adding. Two matrix must has the same shape."
        return Matrix([[i + j for i, j in zip(a, b)] for a, b in zip(self, other)])

    def __sub__(self, other):
        assert self.shape() == other.shape(), "Error in subtracting. Two matrix must has the same shape."
        return Matrix([[i - j for i, j in zip(a, b)] for a, b in zip(self, other)])

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix([[other * i for i in j] for j in self])
        elif type(other) == Vector:
            assert self.col_num() == len(other), "Error in dot."
            return Vector([other.dot(self.row_vector(i)) for i in range(self.row_num())])
        elif type(other) == type(self):
            assert other.row_num() == self.col_num()
            return Matrix([[self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num())] for i in
                           range(self.row_num())])

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return self * other

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return 1 / other * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    @classmethod
    def zero(cls, row: int, col: int):
        return cls([[0] * col for _ in range(row)])

    @classmethod
    def identity(cls, n):
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)
