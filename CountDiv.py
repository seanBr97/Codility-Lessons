"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

# 100% Correctness, 0% Performance O(B-A)
def solution(A, B, K):
    numbers_divisible_by_k = 0
    search_space = set(range(A, B+1))
    if 0 in search_space:
        numbers_divisible_by_k += 1
    multiplical_of_k = K
    search = True
    while search:
        if multiplical_of_k >= B:
            search = False
        if multiplical_of_k in search_space:
            numbers_divisible_by_k += 1
        multiplical_of_k += K
    return numbers_divisible_by_k
    
# 87% Overall, 75% Correctness, 100% Performance O(1)
import math

def solution(A, B, K):
    numbers_divisable_by_k = 0
    if A % K == 0 or B % K ==0:
        numbers_divisable_by_k += 1    
    numbers_divisable_by_k += math.floor((B-A)/K) # number of gaps
    return numbers_divisable_by_k