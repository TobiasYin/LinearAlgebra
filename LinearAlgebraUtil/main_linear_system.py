from LinearAlgebraUtil.LinearSystem import LinearSystem
from LinearAlgebraUtil.Vector import Vector
from LinearAlgebraUtil.Matrix import Matrix

A = Matrix([[1, 2, 4, 5, 7], [3, 7, 2, 3, 4], [2, 3, 3, 4, 2], [1, 2, 5, 4, 9], [3, 4, 5, 1, 7]])
# A = Matrix([[2, 2], [2, 1], [1, 2]])
b = Vector([7, -11, 1, 3, 9])
# b = Vector([3, 2.5, 7])
system = LinearSystem(A, b)
print(system.get_matrix())
ret = system.guass_jordan_elimination()
print(system.get_matrix())
print(ret)