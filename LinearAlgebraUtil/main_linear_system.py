from LinearAlgebraUtil.LinearSystem import LinearSystem
from LinearAlgebraUtil.Vector import Vector
from LinearAlgebraUtil.Matrix import Matrix


A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
b = Vector([7, -11, 1])
system = LinearSystem(A, b)
print(system.get_matrix())
system.guass_jordan_elimination()
print(system.get_matrix())
system.fancy_print()
