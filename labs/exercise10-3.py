import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
import matplotlib.animation as animation

frames = 1800
x_pos = [0]
y_pos = [0]

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))

particle = plt.Circle((0, 0), radius=0.75, fc='c')
ax.add_patch(particle)

line = ax.plot(x_pos, y_pos, c='g', alpha=0.5)[0]


def animate(i):
    pos = particle.center

    x = pos[0]
    y = pos[1]

    direction = rand.random() * 2 * np.pi

    x += np.cos(direction)
    y += np.sin(direction)

    x = np.clip(x, -50, 50)
    y = np.clip(y, -50, 50)

    x_pos.append(x)
    y_pos.append(y)

    print(i, x, y)
    particle.center = (x, y)
    line.set_xdata(x_pos)
    line.set_ydata(y_pos)

    return particle,


anim = animation.FuncAnimation(fig, animate, frames=frames, interval=10)

plt.show()

# pillow_writer = animation.PillowWriter(fps=30)
# anim.save("exercise10-3.gif", pillow_writer)

