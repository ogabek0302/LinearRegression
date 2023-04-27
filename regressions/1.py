import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.randn(100, 1)

model = LinearRegression()
model.fit(x, y)

x_test = np.linspace(0, 1, 100).reshape(-1, 1)
y_pred = model.predict(x_test)

plt.scatter(x, y)
plt.plot(x_test, y_pred, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
