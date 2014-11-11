import math


is_divisor = lambda divisor, multiple: not multiple % divisor

def get_n_divisors(number):
    n_divisors = 1
    current = number
    i = 2
    while current >= i:
        if is_divisor(i, current):
            exponent = 0
            while current and is_divisor(i, current):
                current = current/i
                exponent += 1                
            n_divisors *= exponent + 1
        i += 1
    return n_divisors

n_divisors = 0
i = 1
while n_divisors < 500:
    triangle_number = i*(i + 1)/2
    n_divisors = get_n_divisors(triangle_number)
    i += 1
print triangle_number