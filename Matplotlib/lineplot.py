import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 4, 6, 8, 10, 2, 4, 6]
plt.plot(x, y, 'r-', label = 'life')
'''
change the letter to get new colour
change the - to a o to change the plot from showing dots to a line
for different types of lines you can use -- or -. or : or ...
can specify lines width with plt.plot(x, y, 'r-', linewidth = 2.0)
for dots on screen you can you different types such as o or ^ or s
add your line with your dots to get both the line and dots
'''

plt.axis([0, 10, 0, 10])

plt.xlabel("Horizontal Title")

plt.ylabel("Vertical Title")

plt.title("Line Plot")

plt.show()
