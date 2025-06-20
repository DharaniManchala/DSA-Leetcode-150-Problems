class Solution(object):
    def wordPattern(self, pattern, s):
        
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word

            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch

        return True
    
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))  # Output: True
    print(solution.wordPattern("abba", "dog cat cat fish"))  # Output: False
    print(solution.wordPattern("aaaa", "dog dog dog dog"))  # Output: True
    print(solution.wordPattern("abba", "dog dog dog dog"))  # Output: False
# time complexity: O(n) where n is the length of the string s
# space complexity: O(1) since the character set is fixed (e.g., lowercase English letters)
