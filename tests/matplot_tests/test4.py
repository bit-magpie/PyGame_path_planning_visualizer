import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
a = np.zeros((100,100))
im = ax.imshow(a, cmap='Blues')
cir = Circle((10,10), 1, color='r')

# initialization function: plot the background of each frame
def init():
    im.set_data([[]])
    ax.add_patch(cir)
    return im, cir

# animation function.  This is called sequentially
def animate(i):
    xy = np.random.random(2)*100
    cir.center = xy[0], xy[1]
    return im, cir


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=50, blit=True)


plt.show()