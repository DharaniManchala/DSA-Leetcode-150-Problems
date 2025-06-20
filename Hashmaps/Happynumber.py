class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1:
            if n in seen:
                return False  # loop detected
            seen.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))

        return True
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(19))  # Output: True
    print(solution.isHappy(2))   # Output: False
    print(solution.isHappy(7))   # Output: True
    print(solution.isHappy(4))   # Output: False
# time complexity: O(log n) where n is the number of digits in the number
# space complexity: O(log n) for the set to store seen numbers