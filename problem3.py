# Largest prime number
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime(n):
    if type(n) != int:
        return 'Input must be Integer'
    elif n < 0:
        return 'Number must be positive'
    factors = list()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if is_prime(i):
                factors.append(i)
    return max(factors)


print(largest_prime(600851475143))
