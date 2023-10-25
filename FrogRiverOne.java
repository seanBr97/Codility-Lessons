/*
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
 In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
*/

// 100% - O(N)
import java.util.*;
import java.util.stream.*;

class Solution 
{
    public Set<Integer> generateSetBetween(int start, int end)
    {
        return (Arrays.stream(IntStream.range(start, end).toArray()).boxed().collect(Collectors.toSet()));
    }
    
    public int solution(int X, int[] A)
    {
        int endPosition = X + 1;                                 

        Set<Integer> requiredPositions = generateSetBetween(1, endPosition);
        Set<Integer> encounteredPositions = new HashSet<>();

        for (int i = 0; i < A.length; i++)
        {
            encounteredPositions.add(A[i]);
            if (encounteredPositions.equals(requiredPositions))
                return i;
        }

        return -1;
    }
}