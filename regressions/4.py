import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [])

def animate(frame):
    x = np.linspace(0, 10, 100)
    y = np.sin(x - frame / 10)
    
    line.set_data(x, y)
    
    return line,

animation = FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
