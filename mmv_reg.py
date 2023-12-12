import numpy as np
import matplotlib.pyplot as plt


# Parametri
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


beta = 0.0001

# Inicijalizacija x
x = np.ones(1024)

# Iteracija
for o in range(N):
    for j in range(1024):
        suma = np.sum(R[:, j])
        x1 = x.reshape(32, 32).T
        U = 0
        del_val = 0
        r = (j - 1) // 32  
        s = (j - 1) % 32
        if r - 1 > 0:
            U += x1[r, s] - x1[r - 1, s]
            del_val += 1
            if s - 1 > 0:
                U += x1[r, s] - x1[r - 1, s - 1]
                del_val += 1
            if s + 1 < 32:
                U += x1[r, s] - x1[r - 1, s + 1]
                del_val += 1
        if s - 1 > 0:
            U += x1[r, s] - x1[r, s - 1]
            del_val += 1
        if s + 1 < 32:
            U += x1[r, s] - x1[r, s + 1]
            del_val += 1
        if r + 1 < 32:
            U += x1[r, s] - x1[r + 1, s]
            del_val += 1
            if s - 1 > 0:
                U += x1[r, s] - x1[r + 1, s - 1]
                del_val += 1
            if s + 1 < 32:
                U += x1[r, s] - x1[r + 1, s + 1]
                del_val += 1
        U /= del_val
        if suma == 0:
            x[j] = 0
        else:
            x[j] = x[j] / (suma - beta * U) * ((y / np.dot(R, x)).dot(R[:, j]))

# Rekonstruisana slika
x1 = x.reshape([32, 32])
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('Regularizovana MMV')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()
