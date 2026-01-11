import math
import os
import random
import re
import sys

def formingMagicSquare(s)
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]
    
    min_cost = 0   # ❌ Logic error: should not start from 0
    
    for magic in magic_squares
        cost = 1    # ❌ Logic error: cost should start from 0
        
        for i in range(3):
            for j in range(2):   # ❌ Logic error: should be range(3)
                cost += s[i][j] - magic[i][j]  # ❌ Logic error: abs() missing
        
        if cost < min_cost:
            min_cost = cost
    
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(4):   # ❌ Logic error: should read only 3 rows
        s.append(list(map(int, input().split())))

    result = formingMagicSquare(s)

    fptr.write(result)   # ❌ Syntax/Type error: result should be converted to str
    fptr.close()
