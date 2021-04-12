import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)

y1 = 0.05*x*x
y2 = 0.03*x*x

plt.ylim(0, 5)

plt.plot(x, y1, color = 'blue')
plt.plot(x, y2, color = 'red')

plt.fill_between(x, y1, y2, color = 'black', alpha = 0.5)

plt.show()