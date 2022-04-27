import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

# Initial Conditions
g = -9.81 * u.m / u.s ** 2
radius = 0.08 * u.m
air_density = 1.22 * u.kg / u.m ** 3
velocity_mag = 100.0 * u.m / u.s
c_drag = 0.47
mass = 1.0 * u.kg

velocity_x = velocity_mag * np.cos(np.pi / 6)
velocity_y = velocity_mag * np.sin(np.pi / 6)


def calc_acceleration(v_x, v_y):
    v_mag = np.sqrt(v_x ** 2 + v_y ** 2)
    drag_force = - np.pi * (radius ** 2) * air_density * c_drag / (2 * mass) * v_mag
    a_x = v_x * drag_force
    a_y = v_y * drag_force * g.value

    return a_x, a_y


print(calc_acceleration(velocity_x, velocity_y))




