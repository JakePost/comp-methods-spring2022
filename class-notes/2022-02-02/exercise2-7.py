# Exercise 2.7

# The Catalan number C_n are a sequence of integers important in quantum mechanics and disordered systems.
# They are given by C_0 = 1; C_n+1 = (4n+2)/(n+2)C_n
# Write a program to print the Catalan numbers up to some user specified value.

n: int = 0

value: int = int(input("Please enter an integer for the exclusive upperbound of the series: "))


def catalan_num(i: int) -> float:
    if i == 0:
        return 1.0

    return (4 * i + 2) / (i + 2) * catalan_num(i - 1)


while n <= value:
    print(catalan_num(n))
    n += 1
    if n == value:
        break


# catalan_num = 1
#
#
# while n < value:
#     catalan_num = (4 * n + 2) / (n + 2) * catalan_num
#     print(catalan_num)
#     n += 1
