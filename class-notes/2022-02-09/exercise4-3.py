# Exercise 4.3
# Suppose we have a function f(x) and we want to calculate its derivative at a point x.
# We can do that with a pencil and paper if we know the mathematical form of the function, or we can do it on the
# computer by making use of the definition of the derivative:
# df/fx = lim_{delta -> 0} (f(x + delta) - f(x)) / delta
#
# On the computer we can't actually take the limit as delta goes to zero, but we can get a reasonable
# approximation just by making delta small.
#
# 1) Write a program that defines a function f(x) returning the value x(x-1) using the derivative of the function at
#    x = 1 using the formula above with delta \ 10^{-2}. Calculate the true value of the same derivative
#    analytically and compare with the answer your program gives. The two will not agree perfectly. Why not?
#
# 2) Repeat the calculation for delta = 10^n n={-4, -6, -8, -10, -12, -14}. You should see that the accuracy of
#    the calculation initially gets better as delta gets smaller.


import matplotlib.pyplot as plt


def derivative(f, delta, x):
    return (f(x + delta) - f(x)) / delta


def func(x):
    return x * (x - 1)


print(derivative(func, 10e-2, 1))

x_vals = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
y_vals = [derivative(func, k, 1) for k in x_vals]

figure, axes = plt.subplots(1, 1, figsize=(5, 5))

axes.set_title("Derivative Limit")
axes.set_xscale("log")
axes.set_xticks(x_vals)
axes.axhline(y=1, linestyle='--', alpha=0.3)
axes.scatter(x_vals, y_vals)

plt.show()
