import numpy as np
import matplotlib.pyplot as plt

# Définir la plage de coordonnées
xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
resolution = 1000
maxiter = 100

# Initialiser le tableau pour stocker les valeurs
mandelbrot = np.zeros((resolution, resolution))

# Calculer les valeurs pour chaque point
x = np.linspace(xmin, xmax, resolution)
y = np.linspace(ymin, ymax, resolution)
for i in range(resolution):
    for j in range(resolution):
        c = complex(x[i], y[j])
        z = 0
        for k in range(maxiter):
            z = z ** 2 + c
            if abs(z) > 2:
                mandelbrot[j, i] = k
                break

# Dessiner l'ensemble de Mandelbrot
plt.imshow(mandelbrot.T, cmap='magma', extent=[xmin, xmax, ymin, ymax])
plt.title("L'ensemble de Mandelbrot")
plt.axis('off')
plt.show()
