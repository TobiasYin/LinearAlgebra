import matplotlib.pyplot as plt
import numpy as np

points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
          [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
plt.figure(figsize=(5, 5))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
points_matrix = np.array(points)
plt.plot(points_matrix[:, 0], points_matrix[:, 1])
scale = np.array([[1, 0], [0, -1]])
points_matrix = scale.dot(points_matrix.T).T
plt.plot(points_matrix[:, 0], points_matrix[:, 1])
points_matrix = np.array([[-1, 0], [0, 1]]).dot(np.array(points).T).T
plt.plot(points_matrix[:, 0], points_matrix[:, 1])
points_matrix = np.array([[1, 1 / 2], [0, 1]]).dot(np.array(points).T).T
plt.plot(points_matrix[:, 0], points_matrix[:, 1])
points_matrix = np.array([[1 / 2, 1.7 / 2], [-1.7 / 2, 1 / 2]]).dot(np.array(points).T).T
plt.plot(points_matrix[:, 0], points_matrix[:, 1])
points_matrix = np.array([[1.5, -1], [0, 2]]).dot(np.array(points).T).T
plt.plot(points_matrix[:, 0], points_matrix[:, 1])
plt.show()
