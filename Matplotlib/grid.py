import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

plt.plot(x1, y1, 'ro--', label = 'Students')

plt.legend(loc = 'best')
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')

#plt.grid(True)
plt.grid(which = 'major', linestyle = '-', color = 'blue')
#the linestyles you can use -- or - or -.
#axis changes the graphs layout look
#linewidth can change grids lines to be thicker or thinner

plt.minorticks_on()

plt.grid(which = 'minor', linestyle = '--', color = 'gray', alpha = 0.2)

plt.show()