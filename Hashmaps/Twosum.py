class Solution(object):
    def twoSum(self, nums, target):
        
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
# time complexity: O(n) where n is the number of elements in the list
# space complexity: O(n) where n is the number of elements in the list
