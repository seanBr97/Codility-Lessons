/*
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
*/

import java.util.Arrays;
import java.util.HashMap;
HashMap<Int, Int> item_counts = new HashMap<Int, Int>();

class Solution 
{
    public boolean isOddNumber (int A)
	{
		return (A/2 == 1);
	}
	
	public int solution(int[] A)
	{
        // Implement your solution here
		// sort array, loop w counter, when A[i] != A[i+1] check counter / 2 == 0, if not --> found odd
		
        Arrays.sort(A);
		int numOccurences = 0;
		for (int i = 0; i < A.length - 1; i++)
		{
			int currentNumber = A[i];
			int nextNumber = A[i+1];
			if (currentNumber == nextNumber)
				numOccurences += 1;
			else if (isOddNumber(numOccurences))
				return currentNumber;                        
		}
		return A[A.length - 1];
    }
}