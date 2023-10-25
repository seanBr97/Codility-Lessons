"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""

# 100% O(NlogN)
def solution(A):
    N = len(A)
    A.sort()
    
    # positive case --> we have biggest number = good
    # negative case --> we have the 'smallest' negative number/closest to zero = good
    mul1 = A[N-1]
    
    # positive case
    second_biggest_number = A[N-2]
    third_biggest_number = A[N-3]
    positive_product = mul1 * second_biggest_number * third_biggest_number
    
    # negative case 
    smallest_number = A[0]
    second_smallest_number = A[1]
    negative_product = mul1 * smallest_number * second_smallest_number

    product = max(positive_product, negative_product)
    
    return product