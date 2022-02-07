# Exercise 4.2

# Write a program that takes 3 numbers as input; a, b, and c and prints out two solutions to the quadratic eq.
# Use you program to compute the solutions to 0.001x^2 + 1000x + 0.001 = 0
# There is another way to write the quadratic equation if you multiply the numerator and denominator by
# - b +- sqrt(b^2-4ac), you'll get x = 2c / b +- sqrt(b^2-4ac)
# Add further lines to your program to also use this alternative solution. Do you get the same value for x? Why?

import argparse
import math

parser = argparse.ArgumentParser(description="Solve the quadratic equation for an input of a, b, and c")

parser.add_argument('a', type=float, help='a value in quadratic equation.')
parser.add_argument('b', type=float, help='b value in quadratic equation.')
parser.add_argument('c', type=float, help='c value in quadratic equation.')

args = parser.parse_args()


def quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    denominator = 2 * a
    part_sqrt = math.sqrt((b ** 2) - 4 * a * c)
    pos_numerator = -b + part_sqrt
    neg_numerator = -b - part_sqrt

    return pos_numerator / denominator, neg_numerator / denominator


def alt_quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    numerator = 2 * c
    part_sqrt = math.sqrt((b ** 2) - 4 * a * c)
    pos_denominator = -b + part_sqrt
    neg_denominator = -b - part_sqrt

    return numerator / pos_denominator, numerator / neg_denominator


print(quadratic(args.a, args.b, args.c))
print(alt_quadratic(args.a, args.b, args.c))


