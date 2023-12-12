import numpy as np
import matplotlib.pyplot as plt


rows = 32
cols = 32
num_projections = 40
num_rays_per_projection = 32
N = 50

R = np.loadtxt('R')
y = np.loadtxt('y.txt')
R = np.transpose(R)
y = np.transpose(y)

x = np.zeros(1024)


for i in range(N):
    rays = np.random.permutation(1280)

    for j in range(1280):
        el = rays[j]
        s = (y[el] - np.dot(R[el, :], x)) / np.dot(R[el, :], R[el, :].T) * R[el, :].T
        x = x + s
        x[x < 0] = 0

# Rekonstruisana slika
x1 = x.reshape([32, 32])
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('ART')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()
