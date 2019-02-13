import math
from ._global import EPSILON


class Vector(object):
    def __init__(self, l: list):
        self._values = l.copy()

    @classmethod
    def zero(cls, dim: int):
        return cls([0] * dim)

    def dot(self, other):
        assert len(other) == len(self), "Error in adding, length of vectors must be same."
        return sum(i * j for i, j in zip(self, other))

    def norm(self):
        return math.sqrt(sum(i ** 2 for i in self))

    def normalize(self):
        n = self.norm()
        if n < EPSILON:
            raise ZeroDivisionError("Zero can't be normalized!")
        return Vector(self._values) / n

    def __getitem__(self, index: int):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __iter__(self):
        return self._values.__iter__()

    def __add__(self, other):
        assert len(other) == len(self), "Error in adding, length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(other) == len(self), "Error in adding, length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector([i * other for i in self])

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector([i * other for i in self])

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return (1 / other) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __eq__(self, other):
        other_list = other.underlying_list()
        if len(other_list) != len(self._values):
            return False
        return all([i == j for i, j in zip(other_list, self._values)])

    def __neq__(self, other):
        return not (self == other)

    def underlying_list(self):
        return self._values.copy()
