class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # start of a sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(solution.longestConsecutive([0, -1]))                # Output: 2
    print(solution.longestConsecutive([]))                     # Output: 0
    print(solution.longestConsecutive([1, 2, 0, 1]))          # Output: 3
# time complexity: O(n) where n is the number of elements in the list
# space complexity: O(n) for the set to store unique elements