import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.15
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
# Make your code
# ******************************

fig, ax = plt.subplots()
rect1 = ax.bar(x-width*1.5, Math, width, label='Math')
rect2 = ax.bar(x-width*.5, English, width, label='English')
rect3 = ax.bar(x+width*.5, Physics, width, label='Physics')
rect4 = ax.bar(x+width*1.5, Computer, width, label='Computer')

ax.set_title('Grouped graph for scores')
ax.legend()
ax.set_xticks(x, names)
ax.bar_label(rect1, padding=3)
ax.bar_label(rect2, padding=3)
ax.bar_label(rect3, padding=3)
ax.bar_label(rect4, padding=3)

plt.show

fig.savefig('A11.png')


#import matplotlib.pyplot as plt

#data1 = [100, 90, 80, 60]
#data2 = [90, 80, 70, 100]
#labels = ['Math', 'English', 'Physics', 'Computer']
#names = ['Bill', 'Mary']

#fig, ax = plt.subplots()

#ax.bar(labels, data1, label='Bill')
#ax.bar(labels, data2, bottom=data1, label='Mary')
#ax.legend()
#ax.set_title('Stacked graph for scores')

#plt.show()

#fig.savefig('A10.png')