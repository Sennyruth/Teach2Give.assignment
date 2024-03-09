# Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(n):
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return n == 1

print(is_power_of_two(16))


