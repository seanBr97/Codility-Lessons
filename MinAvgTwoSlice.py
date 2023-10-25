"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.
"""

# 60% Overall 100% Correct 20% Performance O(n^2)
def solution(A):
    
    N = len(A)
    if N == 1:
        return 0

    minimum_average = (A[0] + A[1])/2
    minimum_average_starting_index = 0

    for P in range (0, N):
        slice = A[P]
        for Q in range(P+1, N):
            slice += A[Q]
            slice_average = slice/(Q - P + 1)
            if slice_average < minimum_average:
                minimum_average = slice_average
                minimum_average_starting_index = P

    return minimum_average_starting_index