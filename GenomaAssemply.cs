// C# program to find shortest
// superstring using Greedy
// Approximate Algorithm
using System;

class GFG
{

	static String str;

	// Utility function to calculate
	// minimum of two numbers
	static int min(int a, int b)
	{
		return (a < b) ? a : b;
	}

	// Function to calculate maximum
	// overlap in two given strings
	static int findOverlappingPair(String str1,
								String str2)
	{
		
		// max will store maximum
		// overlap i.e maximum
		// length of the matching
		// prefix and suffix
		int max = Int32.MinValue;
		int len1 = str1.Length;
		int len2 = str2.Length;

		// check suffix of str1 matches
		// with prefix of str2
		for (int i = 1; i <= min(len1, len2); i++)
		{

			// compare last i characters
			// in str1 with first i
			// characters in str2
			if (str1.Substring(len1 - i).CompareTo(
						str2.Substring(0, i)) == 0)
			{
				if (max < i)
				{

					// Update max and str
					max = i;
					str = str1 + str2.Substring(i);
				}
			}
		}

		// check prefix of str1 matches
		// with suffix of str2
		for (int i = 1; i <=min(len1, len2); i++)
		{

			// compare first i characterselse
			// in str1 with last i
			// characters in str2
			if (str1.Substring(0, i).CompareTo(
					str2.Substring(len2 - i)) == 0)
			{
				if (max < i)
				{

					// pdate max and str
					max = i;
					str = str2 + str1.Substring(i);
				}
			}
		}

		return max;
	}

	// Function to calculate smallest
	// string that contains
	// each string in the given set as substring.
	static String findShortestSuperstring(String []arr, int len)
	{
		
		while (len != 1)
		{
			
			int max = Int32.MinValue;
		
			int l = 0, r = 0;
				
				String resStr = "";

			for (int i = 0; i < len; i++)
			{
				for (int j = i + 1; j < len; j++)
				{

					int res = findOverlappingPair
								(arr[i], arr[j]);

					if (max < res)
					{
						max = res;
						resStr = str;
						l = i;
						r = j;
					}
				}
			}

			// Ignore last element in next cycle
			len--;

			// If no overlap,
			// append arr[len] to arr[0]
			if (max == Int32.MinValue)
				arr[0] += arr[len];
			else
			{
			
				// Copy resultant string
				// to index l
				arr[l] = resStr;
			
				// Copy string at last index
				// to index r
				arr[r] = arr[len];
			}
		}
		return arr[0];
	}

	// Driver Code
	public static void Main(String[] args)
	{
		String[] arr = { "ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC" };
		int len = arr.Length;

		Console.Write("The Shortest Superstring is " +
						findShortestSuperstring(arr, len));
	}
}

// This code is contributed by shivanisinghss2110
