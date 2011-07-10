#!/usr/bin/env python

is_multiple = lambda multiple, divisor: not multiple%divisor
is_multiple_of_any = lambda multiple, divisors: any(is_multiple(multiple, divisor) for divisor in divisors)
sum_of_multiples = lambda upper_limit, divisors: sum(multiple for multiple in range(1000) if is_multiple_of_any(multiple, divisors))

print sum_of_multiples(1000, (3, 5))
