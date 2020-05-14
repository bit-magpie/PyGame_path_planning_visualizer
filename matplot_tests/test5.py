import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def velocity_field(xy, t):
    x, y = xy
    vx = -np.sin(2*np.pi * x) * np.cos(2*np.pi * y) \
        - 0.1*np.cos(2 * np.pi * t) * np.sin(2*np.pi*(x - 0.25)) * np.cos(2*np.pi*(y - 0.25))
    vy =  np.cos(2*np.pi * x) * np.sin(2*np.pi * y) \
       + 0.1*np.cos(2*np.pi * t) * np.cos(2*np.pi*(x - 0.25)) * np.sin(2*np.pi*(y - 0.25))
    return (vx, vy)


xy0 = (0, 0)
t_span = np.arange(0, 100, 0.05)

sol = odeint(velocity_field, xy0, t_span)

plt.plot(sol[:, 0], sol[:, 1])
plt.axis('equal'); plt.xlabel('x'); plt.ylabel('y')

initial_conditons = [(1, .4), (1, 0), (4, .7)]
t_span = np.arange(0, 100, 0.05)

plt.figure(figsize=(6, 6))
for xy0 in initial_conditons:
    sol = odeint(velocity_field, xy0, t_span)
    plt.plot(sol[:, 0], sol[:, 1])

plt.axis('equal'); plt.xlabel('x'); plt.ylabel('y')

plt.show()