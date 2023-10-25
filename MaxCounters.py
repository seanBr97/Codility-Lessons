"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

# 100% everything, O(N+M)
# maintain baseline with minimum, but set the values at the very end
# m-1 because A[0] = 3 would be at A[2]
def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_min = 0    
    for m in A:
        if m != N+1:            
            if counters[m-1] < current_min:
                counters[m-1] = current_min
            # current_min = min(current_min, counters[m-1])
            
            counters[m-1] += 1

            if counters[m-1] > max_counter:
                max_counter = counters[m-1]
            # max_counter = max(max_counter, counters[m-1])
        else:
            current_min = max_counter

    for m in range(N):
        if counters[m] < current_min:
            counters[m] = current_min
        # current_min = min(current_min, counters[m])
    return counters

# 100% Correctness 60% Performance O(N*M) 77% Overall
def solution(N, A):
    counters = [0] * N
    max_counter = 0
    for m in A:
        if m != N+1:
            counters[m-1] += 1
            if counters[m-1] > max_counter:
                max_counter = counters[m-1]
        else:
            counters = [max_counter] * N            
    return counters

# 100% Correctness 40% Performance O(N*M) 66% Overall
def solution(N, A):
    counters = [0] * N
    for k in A:
        if k != N+1:
            counters[k-1] += 1
        else:
            counters = [max(counters)] * N
    return counters