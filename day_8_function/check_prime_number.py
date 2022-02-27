#!/usr/bin/env python3
# Python 3.9.6

# Prime number cheker

import time
start_time = time.time()


def prime_cheker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} not a prime number")


prime_cheker(100000)

print("Process finished --- %s seconds ---" % (time.time() - start_time))
