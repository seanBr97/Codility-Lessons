"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution(A, K):
     
    N = len(A)
    # return empty array if input array is empty
    if N == 0:
        return []

    # check if meets entry conditions
    if (N > 0 and N <= 100 and K > 0 and K <= 100):              
        
        # handle K >= N (redundant rotations)
        if K >= N:
            K = K % N
            
        # no rotations
        if K == 0:
            return A
                  
        # do rotations (out of place)                
        rotated_A = [0] * N
        for i in range(N):
            if i + K < N:
                rotated_A[i + K] = A[i]
            else:                
                # N - i - 1 = distance to end of array
                # can ignore the -1 due to 0 indexing
                rotated_A[i - N + K] = A[i]                

        return rotated_A
    else:
        return A
