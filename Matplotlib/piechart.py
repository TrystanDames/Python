import matplotlib.pyplot as plt

values = [16, 18, 4, 8]
pielabels = ['Python', 'Ruby', 'Java', 'Perl']
piecolors = ['red', 'blue', 'orange', 'yellow']
pieexplode = [0.1, 0, 0, 0]

plt.pie(values, labels = pielabels, explode = pieexplode, colors = piecolors, startangle = 90, shadow = True)
#The startangle rotates the pie chart

plt.title('Pie Chart')

plt.xlabel('Horizontal title')

plt.ylabel('Vertical title')

plt.legend(loc = 'best')

plt.show()