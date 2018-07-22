# Interview Bit: https://www.interviewbit.com/problems/longest-consecutive-sequence/
# Given an unsorted array of integers,
# find the length of the longest consecutive elements sequence.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if len(A) == 0:
            return 0

        s = set()
        longest_count = 1

        for x in A:
            s.add(x)

        for x in A:
            left = x - 1
            right = x + 1
            count = 1

            while left in s:
                count += 1
                s.remove(left)
                left -= 1

            while right in s:
                count += 1
                s.remove(right)
                right += 1

            longest_count = max(longest_count, count)

        return longest_count

if __name__ == "__main__":
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])