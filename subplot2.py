import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y1)

plt.subplot(2, 1, 2)
plt.plot(x, y2)

plt.show()
