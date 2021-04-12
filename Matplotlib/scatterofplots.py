import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("darkdrid")

N = 50
x1 = np.random.rand(N)
y1 = np.random.rand(N)
s1 = np.random.rand(N) * 300
x2 = np.random.rand(N)
y2 = np.random.rand(N)
s2 = np.random.rand(N) * 300

plt.scatter(x1, y1,  s = 10)
plt.scatter(x2, y2, s = 30)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')

plt.show()