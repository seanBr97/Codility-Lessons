"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""

# 55% Overall 100% Correct, 0% Performance, N^2 runtime
from collections import Counter

def solution(A):
    N = len(A)
    num_equileaders = 0

    if N == 1:
        return num_equileaders

    S = 1
    left_side_counts = Counter(A[0:1])    
    right_side_counts = Counter(A[1:N])

    for iteration in range(N-1):        
        # check for equileader, add if exists
        if exists_equileader(left_side_counts, right_side_counts):
            num_equileaders += 1                

        # shift left side towards the right
        new_left = A[S]
        # if new_left already exists, increment it's count
        if new_left in left_side_counts.keys():
            left_side_counts[new_left] = left_side_counts[new_left] + 1
        # else, create a count for new_left
        else:
            left_side_counts[new_left] = 1
        
        # shift right side towards the left
        # decrement new_left count
        right_side_counts[new_left] = right_side_counts[new_left] - 1
        # if new_left was the last of this element in the right side, delete the count
        if right_side_counts[new_left] == 0:
            del (right_side_counts[new_left])

        S += 1

    return num_equileaders


def exists_equileader (left, right):
    left_leader = get_leader(left)
    right_leader = get_leader(right)

    left_leader_exists = left_leader != -1
    right_leader_exists = right_leader != -1

    if left_leader_exists and right_leader_exists and left_leader == right_leader:
        return True
    else:
        return False    

def get_leader (counts):
    most_common_number_tuple = counts.most_common(1)[0]
    most_common_number = most_common_number_tuple[0]
    most_common_number_frequency =  most_common_number_tuple[1]
    if most_common_number_frequency > get_N(counts)/2:
        return most_common_number
    else:
        return -1

def get_N (counts):
    N = 0
    for key in counts.keys():
        N += counts[key]
    return N