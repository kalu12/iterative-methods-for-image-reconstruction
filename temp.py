import numpy as np
import matplotlib.pyplot as plt


# Parametri
rows = 32
cols = 32
num_iterations = 1000
lambda_value = 0.01

# Učitavanje matrice sistema R i vektora y
# Prilagodite putanje do vaših fajlova
R = np.loadtxt('R')
R = np.transpose(R);    
y = np.loadtxt('y.txt')
y = np.transpose(y)


plt.imshow(y.reshape(32 ,40), cmap='gray', vmin=0, vmax=1)
plt.title('Sinogram')
plt.show()



# Parametri
lambda_value = 0.01
N = 1000  # Broj iteracija

# Inicijalizacija x
x = np.zeros(R.shape[1])


# Inicijalizacija hi
hi = np.zeros(N)

# Iterativna metoda najmanjih kvadrata
for i in range(N):
    x = x + lambda_value * R.T @ (y - R @ x)
    hi[i] = np.sum((y - R @ x) ** 2)
    x[x < 0] = 0

# Rekonstruisana slika
x1 = x.reshape((32, 32)).T
plt.figure()
plt.imshow(x1, cmap='gray', vmin=0, vmax=1)
plt.colorbar(orientation='vertical')
plt.title('Metoda najmanjih kvadrata')
plt.xlabel('Index pixela')
plt.ylabel('Index pixela')
plt.show()

# Prikaz grafika euklidske norme
plt.figure()
iterations = np.arange(1, N + 1)
plt.plot(np.log(iterations), hi)
plt.title('Euklidska norma za MNK')
plt.xlabel('Broj iteracija (logaritamska skala)')
plt.ylabel('Euklidska norma')
plt.show()
