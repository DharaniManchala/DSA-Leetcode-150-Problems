class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in s_to_t:
                if s_to_t[ch_s] != ch_t:
                    return False
            else:
                s_to_t[ch_s] = ch_t

            if ch_t in t_to_s:
                if t_to_s[ch_t] != ch_s:
                    return False
            else:
                t_to_s[ch_t] = ch_s

        return True
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))  # Output: True
    print(solution.isIsomorphic("foo", "bar"))  # Output: False
    print(solution.isIsomorphic("paper", "title"))  # Output: True
    print(solution.isIsomorphic("ab", "aa"))  # Output: False

# time complexity: O(n) where n is the length of the strings
# space complexity: O(1) since the character set is fixed (e.g., lowercase English letters)
