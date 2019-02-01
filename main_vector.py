from LinearAlgebraUtil.Vector import Vector

vec = Vector([5, 2])
print(vec)
print(vec[0])

vec2 = Vector([3, 1])
print(vec + vec2)

print(vec * 2)
print(-vec)
print(+vec)
print(Vector.zero(4))
print(vec.zero(3))
zero = Vector.zero(2)
print(vec + zero)
print(vec.norm())
print(vec.normalize().norm())
print(vec / 2)

print(vec2.dot(vec))
