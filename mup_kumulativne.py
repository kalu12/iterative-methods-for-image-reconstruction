import numpy as np
import matplotlib.pyplot as plt

# Parametri
rows = 32
cols = 32
N = 1


R = np.loadtxt('R')
y = np.loadtxt('y.txt')
R = np.transpose(R)
y = np.transpose(y)


x = np.ones(1024)


for o in range(N):
    for j in range(1024):
        for n in range(40, 1281, 40):
            if np.sum(R[:n, j]) == 0:
                continue
            pom = np.dot(R[:n, :], x)
            pom[pom == 0] = 0.0001
            suma = np.sum(R[:n, j] / pom * y[:n])
            x[j] = x[j] / np.sum(R[:n, j]) * suma

# Rekonstruisana slika
x1 = x.reshape([32, 32])
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('Metoda uređenih podgrupa (kumulativne)')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()
