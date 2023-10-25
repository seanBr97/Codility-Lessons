"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] 
and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] 
+ ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second 
part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""

# Correctness 100% 0% Performance O(N^2) 53% Overall
def solution(A):
    N = len(A)
    smallest_difference = abs(A[0] - sum(A[1:N])) # the first possible answer
    for split in range (1, N):                
        left_split = sum(A[0:split])
        right_split = sum(A[split:N])
        difference = abs(left_split - right_split)
        if difference < smallest_difference:
            smallest_difference = difference
        # smallest_difference = min(smallest_difference, difference)
    return smallest_difference

# Correctness 85% (failed case is wrong imo) Performance 100% O(N) Overall 92%
def solution(A):
    N = len(A)
    previous_left_sum = sum(A[0:1])  # first left split
    previous_right_sum = sum(A[1:N]) # first right split
    smallest_difference = abs(previous_left_sum - previous_right_sum)
    
    if N == 2:
        return smallest_difference
        
    # maintaining previous sums between loops
    for split in range (1, N):  # N-1 gives 100% correctness. Unsure why as P < N condition is true regardless?                
                                # think it's because i<N (N-1 cuz of indexing) results in an empty right split
        left_split = previous_left_sum + A[split]
        right_split = previous_right_sum - A[split]
        difference = abs(left_split - right_split)
        if difference < smallest_difference:
            smallest_difference = difference
        # smallest_difference = min(smallest_difference, difference)
        previous_left_sum = left_split
        previous_right_sum = right_split      

    return smallest_difference
    