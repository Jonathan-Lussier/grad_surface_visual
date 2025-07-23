import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Define a smoother cost function with fewer and smaller peaks/valleys
def smoother_cost_function(theta0, theta1):
    return (
        (0.5 * np.sin(1.5 * np.pi * theta0) * np.cos(1.5 * np.pi * theta1)
        + 0.5 * np.exp(-((theta0 - 0.6)**2 + (theta1 - 0.6)**2) * 5)
        - 0.2 * np.exp(-((theta0 - 0.3)**2 + (theta1 - 0.7)**2) * 10)
        
        +0.5)*10
                )

# Create a high-resolution grid
theta0_vals = np.linspace(0, 1, 1000)
theta1_vals = np.linspace(0, 1, 1000)
theta0_grid, theta1_grid = np.meshgrid(theta0_vals, theta1_vals)

# Evaluate cost function on the grid
J_vals = smoother_cost_function(theta0_grid, theta1_grid)

# Plotting the 3D surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(
    theta0_grid, theta1_grid, J_vals,
    cmap='jet', alpha=0.9, linewidth=0, antialiased=True
)
ax.view_init(elev=35, azim=-145, roll=0)
ax.set_zlim(bottom = 0, top = 25)
# Axis labels
ax.set_xlabel(r'Neuron 1')
ax.set_ylabel(r'Neuron 2')
ax.set_zlabel(r'Loss')

plt.tight_layout()
plt.show()