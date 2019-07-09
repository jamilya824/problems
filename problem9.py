# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def is_pythagorean(x, y, z):
    if x**2+y**2 == z**2:
        return True
    return False


for i in range(1000):
    for j in range(i, 1000-i):
        for k in range(j, 1000-j):
            if i+j+k == 1000:
                if is_pythagorean(i, j, k):
                    result = i*j*k

print(result)