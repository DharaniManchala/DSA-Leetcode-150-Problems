from collections import Counter
def can_construct_ransom_note(ransom_note: str, magazine: str) -> bool:
    # Count the frequency of each character in the magazine
    magazine_count = Counter(magazine)
    
    # Count the frequency of each character in the ransom note
    ransom_note_count = Counter(ransom_note)
    
    # Check if each character in the ransom note can be constructed from the magazine
    for char, count in ransom_note_count.items():
        if magazine_count[char] < count:
            return False
            
    return True
# Example usage
if __name__ == "__main__":
    ransom_note = "aa"
    magazine = "aab"
    print(can_construct_ransom_note(ransom_note, magazine))  # Output: True

    ransom_note = "aa"
    magazine = "ab"
    print(can_construct_ransom_note(ransom_note, magazine))  # Output: False


    # time complexity: O(n + m) where n is the length of the ransom note and m is the length of the magazine
    # space complexity: O(1) since the character set is fixed (e.g., lowercase English letters)