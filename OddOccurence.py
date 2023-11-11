"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.
"""

# didn't realise --> doesn't have to occur just once, can be three times (any odd number of times) 66%
def solution(A):
    
    N = len(A)
    # check list is an odd list
    if (N % 2 == 0):
        return None

    # single element input
    if N == 1:
        return A[0]

    A.sort()
    
    # Case where the unique element is the very first element in the sorted array
    if A[0] != A[1]:
        return A[0]
    # Case where the unique element is the very last element in the sorted array
    elif A[N - 1] != A[N - 2]:
        return A[N - 1]

    # Searching in between the first and last elements of the sorted array
    i = 0
    while (i < N - 2):                
        if (A[i] != A[i + 1]) and (A[i + 1] != A[i + 2]):
            return A[i + 1]
        i += 1
        
# Counter also an option
# with assumption of one occurence
def solution(A):
    # Return minimum occuring character (the answer) 
    count_dict = Counter(A)       
    return int(min(count_dict, key = count_dict.get))

# with multiple occurences 100% Detected time complexity: O(N) or O(N*log(N))
from collections import Counter

def solution(A):    
    count_dict = Counter(A)
    # search for the element which occurs an odd number of times
    odd_number = 1
    while 1:
        if odd_number in list(count_dict.values()):
            return int((list(count_dict.keys())[list(count_dict.values()).index(odd_number)]))
        odd_number += 2        
        
        # could also loop through dict values, divide by 2, odd --> get keys[indexOf(odd_value)]   

# ALTERNATIVE SOLUTION
"""
sort array
loop through it
maintain count of current number
when current_num != next num (i.e. counting of current number is finished)
check odd (%2 == 0) --> return
"""