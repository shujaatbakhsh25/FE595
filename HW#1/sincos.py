import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.1)

y = np.sin(x)
z = np.cos(x)
w = np.tan(x)

plt.plot(x, y, x, z, x, w)
plt.show()
