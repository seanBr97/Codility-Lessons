"""
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.
"""

# 100%
def get_factor_pairs(N):    
    if N == 1:
        return [[1, 1]]
        
    factors = []
    i = 1
    while i*i < N:
        if N % i == 0:            
            factors.append([i, N/i])
        i +=1                       
        if i*i == N:
            factors.append([i, i])
    return factors

# POSSIBLE CHANGE: prevent two divisions --> get N/i, if N/i - floor(N/i) == 0 --> factor (dk if more efficient, maybe slightly)

def get_perimeter(A, B):
    return 2 * (A+B)

def solution(N):
    factor_pairs = get_factor_pairs(N)
    minimum_perimeter = float('inf')
    for pair in factor_pairs:
        perimeter = get_perimeter(pair[0], pair[1])        
        minimum_perimeter = min(minimum_perimeter, perimeter)
    return int(minimum_perimeter) # wants int output, didn't actually specify in the question
