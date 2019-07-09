# Smallest multiple
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?


def divisible(n):
    for i in range(1, 20):
        if n % i != 0:
            return False
    return True


def smallest():
    n = 2520
    while True:
        if divisible(n):
            return n
        n += 20


print(smallest())