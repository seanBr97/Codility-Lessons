"""
Get number of factors of a number N
"""

# 100% O(sqrt(N))

def solution(N):    
    if N == 1:
        return 1
    
    num_factors = 0
    i = 1
    while i*i < N:
        if N % i == 0:
            num_factors += 2        # exploiting that if 2 is a factor of 10, so is 5.
        i +=1                       # and by stopping at sqrt(N), we don't reach 5 so we can double count
        if i*i == N:
            num_factors += 1        # double factor is the same number so +1
    return num_factors