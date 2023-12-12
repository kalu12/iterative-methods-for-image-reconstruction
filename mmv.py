import numpy as np
import matplotlib.pyplot as plt



rows = 32
cols = 32
num_iterations = 1000
lambda_value = 0.01
N = 50

R = np.loadtxt('R')
R = np.transpose(R);    
y = np.loadtxt('y.txt')
y = np.transpose(y)


plt.imshow(y.reshape(40 ,32), cmap='gray', vmin=0, vmax=1000)
plt.title('Sinogram')
plt.xlabel('Snop');
plt.ylabel('Projekcija');
plt.show()




x = np.ones(1024)

# Iteracija
for o in range(N):
    for j in range(1024):
        suma = np.sum(R[:, j])
        if suma == 0:
            x[j] = 0
        else:
            x[j] = x[j] / suma * ((y / np.dot(R, x)).dot(R[:, j]))

# Rekonstruisana slika
x1 = x.reshape([32, 32])
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('Metoda maksimalne verodostojnosti')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()
