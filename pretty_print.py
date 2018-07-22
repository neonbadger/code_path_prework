# https://www.interviewbit.com/problems/prettyprint/
# Print concentric rectangular pattern in a 2d matrix.

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = 2 * A - 1
        arr = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            for j in range(i, size - i):
                arr[i][j] = A - i
                arr[j][i] = A - i
                arr[size - 1 - i][j] = A - i
                arr[j][size - 1 - i] = A - i
        return arr

if __name__ == "__main__":
    s = Solution()
    print s.prettyPrint(2)
    print s.prettyPrint(3)