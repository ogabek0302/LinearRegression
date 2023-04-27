import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update(num):
    line.set_ydata(np.sin(x + 0.1*num))
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
