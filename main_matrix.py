from LinearAlgebraUtil.Matrix import Matrix
from LinearAlgebraUtil.Vector import Vector
from LinearAlgebraUtil.GramSchmidtProcess import gram_schmidt_process
from LinearAlgebraUtil.GramSchmidtProcess import qr
from LinearAlgebraUtil.LinearSystem import inv

m = Matrix([[1, 2], [3, 4]])
print(m)
print(m.shape())
print(m.size())
print(m[0, 1])
print(m.row_vector(1))
n = Matrix([[5, 6], [7, 8]])
print(m + n)
print(m * 2)
print(m / 2)
print(m - n)
print(Matrix.zero(3, 4))
vec = Vector([1, 2])
print(n * vec)
m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
print(m2 * m1)
T = Matrix([[1.5, 0], [0, 2]])
vec1 = Vector([5, 3])
print(T * vec1)
P = Matrix([[0, 4, 5], [0, 0, 3]])
print(T * P)
print(m1.T())
print(Matrix.identity(3))

A = [Vector([1, 2]), Vector([3, 4])]
print(gram_schmidt_process(A))
q, r = qr(Matrix(A))
i = inv(Matrix(A))
print(q)
print(i)
print(q*r)