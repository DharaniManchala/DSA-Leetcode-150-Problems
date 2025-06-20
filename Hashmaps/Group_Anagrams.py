from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort letters
            anagram_groups[sorted_word].append(word)

        return list(anagram_groups.values())
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    
    print(solution.groupAnagrams([""]))  
    # Output: [['']]
    
    print(solution.groupAnagrams(["a"]))  
    # Output: [['a']]
# Output: [['a']]
# time complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string
# space complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
# Note: The sorting operation for each string takes O(k log k) time, and we do this for n strings.