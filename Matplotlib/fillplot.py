import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = 0.05*x*x

plt.ylim(0, 5)

plt.plot(x, y)

plt.fill_between(x, y, color = 'red', alpha = 0.5)

plt.show()