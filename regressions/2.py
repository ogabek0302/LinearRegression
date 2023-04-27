import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

model = LinearRegression()
model.fit(x, y)

x_new = np.array([[0.5], [0.6], [0.7]])
y_pred = model.predict(x_new)

plt.scatter(x, y)
plt.plot(x_new, y_pred, color='red')
plt.show()
