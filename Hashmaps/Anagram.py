from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # Output: True
    print(solution.isAnagram("rat", "car"))          # Output: False
    print(solution.isAnagram("listen", "silent"))    # Output: True
    print(solution.isAnagram("hello", "world"))      # Output: False
# time complexity: O(n) where n is the length of the strings s and t
# space complexity: O(1) since the character set is fixed (e.g., lowercase English letters)