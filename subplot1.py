import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# Create the subplots
fig, axs = plt.subplots(2, 2)

# Plot the data on each subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('sin')
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('cos')
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('tan')
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('exp')

# Add a title for the overall figure
fig.suptitle('Title of Figure')

# Show the plot
plt.show()

