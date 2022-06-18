import sys
import os
import math


def prime(s):

    if s <= 1:
        return False
    if s <= 2:
        return True

    max_divisor = math.ceil(math.sqrt(s)) + 1
    for i in range(2, max_divisor):
        if s % i == 0:
            return False
    return True
    # your code goes here


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
