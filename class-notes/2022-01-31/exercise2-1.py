# Exercise 2.1: Another ball dropped from a tower

# A ball is dropped from a tower of height h with initial velocity zero. Write a program that asks the user to enter the
# height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground,
# ignoring air resistance, Use your program to calculate the time for a ball dropped from a 100 m high tower.

import math
import sys

g = 9.81
userInput = sys.argv[1]

try:
    towerHeight = float(userInput)

    print("The height of the tower is {:3.3f}m".format(towerHeight))

    fallTime = math.sqrt((2 * towerHeight) / g)

    print("The time it takes the ball to fall to the ground is {:3.1f} seconds.".format(fallTime))

except ValueError:
    print("The height of the tower must be inputted as an integer or a float.")
