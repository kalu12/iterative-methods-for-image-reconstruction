import numpy as np
import matplotlib.pyplot as plt

# Parametri
rows = 32
cols = 32
num_iterations = 1000
lambda_value = 0.01
N = 50

R = np.loadtxt('R')
R = np.transpose(R)  
y = np.loadtxt('y.txt')
y = np.transpose(y)

plt.imshow(y.reshape(40, 32), cmap='gray', vmin=0, vmax=1000)
plt.title('Sinogram')
plt.xlabel('Snop');
plt.ylabel('Projekcija');
plt.show()


x = np.ones(1024)

R_sum_j = np.sum(R, axis=1)


for p in range(N):
    for j in range(1024):
        suma = np.sum((R[:, j] * (y - np.dot(R, x)) / R_sum_j) / R_sum_j)
        x[j] = x[j] + suma

x1 = x.reshape([32, 32])
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('SIRT')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()
