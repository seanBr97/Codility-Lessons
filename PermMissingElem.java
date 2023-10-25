/*
An array A consisting of N different integers is given. The array contains integers in the 
range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.
*/

// Solution 1 --> Using Full Sum vs Actual Sum
// 100 % - O(N) or O(N * log(N))
import java.util.Arrays;
import java.util.stream.IntStream;

class Solution 
{

    public int solution(int[] A) 
    {

        int sum = Arrays.stream(A).sum();
        int N = A.length;

        int fullSum = Arrays.stream(IntStream.range(1, N + 2).toArray()).sum();

        int missingElement = fullSum - sum;

        return missingElement;
    }
}

// Solution 2 --> Using Sorting + for loop
import java.util.Arrays;

class Solution 
{
    public int solution(int[] A) 
    {
        Arrays.sort(A);
        int search = 1;
        for (int i = 0; i < A.length; i ++)
        {
            if (A[i] != search)
                return search;

            search ++;
        }

        return -1;
    }
}