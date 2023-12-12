import numpy as np
import matplotlib.pyplot as plt


# Parametri
rows = 32
cols = 32
num_iterations = 1000
lambda_value = 0.01
N = 1000

R = np.loadtxt('R')
R = np.transpose(R);    
y = np.loadtxt('y.txt')
y = np.transpose(y)


plt.imshow(y.reshape(40 ,32), cmap='gray', vmin=0, vmax=1000)
plt.title('Sinogram')
plt.xlabel('Snop');
plt.ylabel('Projekcija');
plt.show()

lambda_value = 0.01


x = np.ones(1024)

E = np.eye(1024)

alfa = float(input('Uneti parametar regularizacije alfa: '))


for i in range(N):
    x = x + lambda_value * R.T @ (y - R @ x) - alfa * E @ x
    x[x < 0] = 0

# Prikaz rezultata za nulti red regularizacije
x0 = x.reshape([32, 32])
plt.figure()
plt.imshow(x0, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('Regularizovana MNK nultog reda')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


C = np.eye(1024)
for i in range(1024):
    for j in range(1024):
        if i == j and 1 < i < 1024:
            C[i, j] = 2
        elif abs(i - j) == 1:
            C[i, j] = -1


x = np.zeros(1024)


for i in range(N):
    x = x + lambda_value * R.T @ (y - R @ x) - alfa * C @ x
    x = np.maximum(x, 0)

# Prikaz rezultata za prvi red regularizacije
x1 = x.reshape([32, 32]).T
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('Regularizovana MNK prvog reda')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
