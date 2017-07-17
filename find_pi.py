import sys
import math
from decimal import *
from math import factorial

def arctan(x):
    """
    Calculate arctan(1/x)

    arctan(1/x) = 1/x - 1/3*x**3 + 1/5*x**5 - ... (x >= 1)

    This calculates it in fixed point, using the value for one passed in
    """
    x = Decimal(x)

    total = Decimal(0)
    sign = 1
    for i in range(1, 512, 2):
        total += sign / (i * x ** i)
        sign = -sign
    return total



def find_pi(n):
    """Find PI to the Nth Digit -
    Enter a number and have the program
    generate PI up to that many decimal places.
     Keep a limit to how far the program will go."""
    num = 4 * (4 * arctan(5) - arctan(239))
    counted = str(num)
    print(counted)
    new_c = counted[:n+2]
    return new_c



def main():
    n = int(input())
    print(find_pi(n))


if __name__ == "__main__":
    main()