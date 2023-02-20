import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure with two subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot the first subplot
ax[0].plot(x, y1)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y1')
ax[0].set_title('sin(x)')

# Plot the second subplot
ax[1].plot(x, y2)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y2')
ax[1].set_title('cos(x)')

# Show the plot
plt.show()
