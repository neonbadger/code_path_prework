# https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/
# Find the kth smallest element in an unsorted array of non-negative integers.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        new_arr = sorted(A)
        return new_arr[B - 1]

if __name__ == "__main__":
    s = Solution()
    print s.kthsmallest([2, 1, 4, 3, 2], 3)