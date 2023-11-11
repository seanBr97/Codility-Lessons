"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
"""

# 100% O(N*log(N))
def solution(A):
    
    sorted_A = sorted(A)

    for P in range(len(sorted_A) - 2):
        Q = P + 1
        R = Q + 1
        if (sorted_A[P] + sorted_A[Q] > sorted_A[R]) and (sorted_A[Q] + sorted_A[R] > sorted_A[P]) and (sorted_A[R] + sorted_A[P] > sorted_A[Q]):
            return 1

    return 0