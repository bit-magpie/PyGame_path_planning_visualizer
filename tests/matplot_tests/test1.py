import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import time

a = np.zeros((100,100))

a[5,5:95] = 1
a[5:95,5] = 1
a[95,5:95] = 1
a[5:96,95] = 1

# a[1,1] = 0.5

plt.ion()
fig, ax = plt.subplots()

cir = Circle((10,10), 1, color='r')
cir2 = Circle((10,90), 1, color='g')
cir3 = Circle((90,90), 1, color='b')
cir4 = Circle((90,90), 1, color='y')

ax.add_patch(cir)
ax.add_patch(cir2)
ax.add_patch(cir3)
ax.add_patch(cir4)
im = ax.imshow(a,cmap='Blues')

i = 10
f = True
while 1:

    cir.center = i,i
    cir2.center = i, 100 - i
    cir3.center = 100 - i, 100 - i
    cir4.center = 100 - i, i
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

    if f:
        i += 1
    else:
        i -= 1

    if i>94:
        f = False
    elif i<6:
        f = True

plt.show()