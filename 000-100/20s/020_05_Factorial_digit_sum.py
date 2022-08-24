"""
## Factorial digit sum

Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Link: https://projecteuler.net/problem=20

Date solved:  
2022/03/21
"""

ANSWER = 648

# imports

from maths.math import sumOfDigits, factorial

# solution


def solution(bypass=False):
    if bypass:
        return ANSWER
    return sumOfDigits(factorial(100))


if __name__ == "__main__":
    solution(bypass=False)
