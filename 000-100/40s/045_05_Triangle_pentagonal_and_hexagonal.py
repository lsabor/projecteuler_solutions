"""
## Triangular, pentagonal, and hexagonal
Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:  
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...  
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...  
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...  

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.


Link: https://projecteuler.net/problem=45

Date solved:  
2022/07/10
"""

ANSWER = 1533776805

# imports

from maths.sequences import TriangleNumbers, PentagonalNumbers, HexagonalNumbers

# solution

T = TriangleNumbers()
P = PentagonalNumbers()
H = HexagonalNumbers()


def get_next_polygonal_number(i: int):
    while True:  # TODO: refactor for iteration through T
        n = T[i + 1]
        if P._isInSetSpecified(n) and H._isInSetSpecified(n):
            return n
        i += 1


def solution(bypass=False):
    if bypass:
        return ANSWER

    i = 286  # the 285th triangle number is a polygonal number, we have to find next
    return get_next_polygonal_number(i)


if __name__ == "__main__":
    from time import perf_counter

    t0 = perf_counter()
    sol = solution(bypass=False)
    t1 = perf_counter()
    print(f"solution = {sol} in {t1-t0: 0.4f} seconds")
    print("answer   =", ANSWER)
