"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
"""

# 87% correctness 0% Performance N^2 complexity
def solution(A):    
    number_of_circles = len(A)
    number_of_intersections = 0
    point_spreads = []
    for centre_point, radius in enumerate(A):                
        left_most_point = centre_point - radius
        right_most_point = centre_point + radius
        point_spreads.append(set(range(left_most_point, right_most_point+1)))
    for i in range(number_of_circles-1):
        current_circle_spread = point_spreads[i]
        j = i + 1        
        for j in range(j, number_of_circles):
            next_circle_spread = point_spreads[j]
            intersections = current_circle_spread.intersection(next_circle_spread)
            if len(intersections) > 0:
                number_of_intersections += 1
            
            if number_of_intersections > 10000000:
                return -1

    return number_of_intersections 
    
# could rule out certain comparisons
# centre1 + radius1 < centre2 - radius2 (right most won't touch left most)