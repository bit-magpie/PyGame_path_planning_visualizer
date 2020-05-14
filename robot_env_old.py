import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle
import time


class Robot():
    def __init__(self, speed=1, size=1, color='r'):
        self.speed = speed
        self.size = size
        self.color = color
        
    def init_robot(self, init_pos=(0,0)):
        self.robot = Circle(init_pos, self.size, color=self.color)
        return self.robot

    def set_position(self, position):
        self.robot.center = position[0], position[1]

class Environment():
    def __init__(self, size=(100,100)):
        self.base = np.zeros(size)  
        self.fig, self.ax = plt.subplots()
        plt.ion()

    def set_obstacles(self):
        self.base[5,5:95] = 1
        self.base[5:95,5] = 1
        self.base[95,5:95] = 1
        self.base[5:96,95] = 1
        self.base[45:60,43:45] = 1
        self.base[20:22,64:80] = 1

    def init_env(self):     
        self.im = self.ax.imshow(self.base, cmap='Blues')   
        plt.show()

    def add_robot(self, robot):
        self.ax.add_patch(robot)

    def update(self):
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


if __name__ == '__main__':
    env = Environment()
    env.set_obstacles()    

    rb1 = Robot()
    rb2 = Robot(color='g')
    env.add_robot(rb1.init_robot((20,10)))
    env.add_robot(rb2.init_robot((10,30)))
    env.init_env()

    for i in range(80):
        rb1.set_position([i,i+2])
        env.update()
        time.sleep(0.5)
    