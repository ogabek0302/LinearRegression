import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.linear_model import LinearRegression

np.random.seed(1)
x = np.random.rand(500)
y = 2 * x + 1 + np.random.randn(500)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y)

line, = ax.plot([], [], color='red')

lr = LinearRegression()

def update(i):
    line.set_data(x[:i], y[:i])
    if i > 0:
        lr.fit(x[:i].reshape(-1, 1), y[:i].reshape(-1, 1))
        line2.set_data(x[:i], lr.predict(x[:i].reshape(-1, 1)))
    return line, line2

line2, = ax.plot([], [], color='black')

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=100)

plt.show()
