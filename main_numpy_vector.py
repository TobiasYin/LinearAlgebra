import numpy as np

if __name__ == "__main__":
    vec = np.array([1, 2, 3, 4, 5])
    print(vec)
    zero = np.zeros(5)
    print(vec.dot(zero))
    print(zero.size)
