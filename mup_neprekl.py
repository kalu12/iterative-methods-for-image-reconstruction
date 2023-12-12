import numpy as np
import matplotlib.pyplot as plt

# Parametri
rows = 32
cols = 32
N = 1

# Učitavanje matrice sistema R i vektora y
# Prilagodite putanje do vaših fajlova
R = np.loadtxt('R')
y = np.loadtxt('y.txt')
R = np.transpose(R)
y = np.transpose(y)
# Metoda uređenih podgrupa (nepreklapajuće)
x = np.ones(1024)


for o in range(N):
    for j in range(1024):
        for n in range(1, 41):
            if np.sum(R[(n-1)*32:n*32, j]) == 0:
                continue
            pomoc = np.dot(R[(n-1)*32:n*32, :], x)
            pomoc[pomoc == 0] = 0.0001  # rešava problem deljenja sa nulom
            suma = np.sum(R[(n-1)*32:n*32, j] / pomoc * y[(n-1)*32:n*32])
            x[j] = x[j] / np.sum(R[(n-1)*32:n*32, j]) * suma

# Rekonstruisana slika
x1 = x.reshape([32, 32])
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1000)
plt.colorbar(orientation='vertical')
plt.title('Metoda uredjenih podgrupa (nepreklapajuće)')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()
