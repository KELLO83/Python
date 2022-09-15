import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')
x = np.arange(0, 10)
y = np.v
z =np.arange(0, 10)
ax.plot(x, y, z)

plt.show()

