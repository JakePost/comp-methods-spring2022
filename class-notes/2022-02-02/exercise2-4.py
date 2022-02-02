# Exercise 2.4:

# A spaceship travels from Earth in a straight line at relativistic speed v to another planet x light years away.
# Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c,
# then print out the time in years that the spaceship takes to reach its destination (a) in the rest frame of an
# observer on Earth and (b) as perceived by a passenger on board the ship.
# Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.

import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Calculate the time it will take a spaceship traveling at relativistic speeds to reach its destination.")

parser.add_argument('d', type=float, help='distance the spaceship will travel in light years.')
parser.add_argument('v', type=float, help='speed of the spaceship as a fraction of the speed of light.')

args = parser.parse_args()


def lorentz_factor(v: float) -> float:
    return 1 / np.sqrt(1 - v ** 2)


passenger_frame = args.d / args.v

earth_frame = passenger_frame * lorentz_factor(args.v)

print("Traveling at {:0.2f}c, {:0.2f} year(s) would pass for the passenger before they reach their destination.".format(args.v, passenger_frame))
print("On earth the observer would see the passenger reach their destination in {0:0.2f} years(s).".format(earth_frame))
