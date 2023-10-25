/*
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
*/

import java.util.Arrays;

class Solution 
{
    public int solution(int[] A) 
    {
        // int[] slicedArray = Arrays.copyOfRange(array, startIndex, endIndex); #            
        int N = A.length;

        int previousLeftSum = Arrays.stream(Arrays.copyOfRange(A, 0, 1)).sum();
        int previousRightSum = Arrays.stream(Arrays.copyOfRange(A, 1, N)).sum();
        int smallestDifference = Math.abs(previousLeftSum - previousRightSum);

        if (N == 2)
            return smallestDifference;

        for (int split = 1; split < N; split++)
        {
            int leftSum = previousLeftSum + A[split];
            int rightSum = previousRightSum - A[split];
            int difference = Math.abs(leftSum - rightSum);

            if (difference < smallestDifference)
                smallestDifference = difference;

            previousLeftSum = leftSum;
            previousRightSum = rightSum;
        }

        return smallestDifference;
    }
}