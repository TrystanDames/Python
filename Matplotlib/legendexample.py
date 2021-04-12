import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]
y2 = [1, 1, 2, 3, 5]

plt.plot(x1, y1, 'ro-', label = 'students')
plt.plot(x1, y2, 'b^-', label = 'teachers')

plt.subplots_adjust(right = 0.7, bottom = 0.3)
plt.legend(bbox_to_anchor = (1.05, 1))
'''
You can specify where you want the legend in the grid using
right/ upper right/ lower right/ left/ upper left/ lower left/ center/ best
if i want legend bottom right I will put for the bbox anchor (1.05, 0) loc = 'lower left'
if i want the legend on the left i would have to move the subplot by changing in subplots_adjust() right to left = 0.3
'''

plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')
plt.grid(True)

plt.show()