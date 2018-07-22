# https://www.interviewbit.com/problems/nextgreater/
# Given an array, find the next greater element G[i] for every element A[i] in the array.
# The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array.
# Elements for which no greater element exist, consider next greater element as -1.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        new_arr = []
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[j] > A[i]:
                    new_arr.append(A[j])
                    break
                elif j == (len(A) - 1):
                    new_arr.append(-1)

        return new_arr

if __name__ == "__main__":
    s = Solution()
    print s.nextGreater([4, 5, 2, 10])
    print s.nextGreater([3, 2, 1])
