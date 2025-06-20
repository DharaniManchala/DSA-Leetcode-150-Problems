class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map:
                if i - index_map[num] <= k:
                    return True
            index_map[num] = i

        return False
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
    print(solution.containsNearbyDuplicate([1, 2, 3, 4, 5], 0))  # Output: False
#     print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False
#     print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3))  # Output: True
# time complexity: O(n) where n is the number of elements in the list
# space complexity: O(n) where n is the number of elements in the list