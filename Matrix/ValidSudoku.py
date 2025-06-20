class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)  # ✅ FIXED HERE

                box_index = (r // 3) * 3 + (c // 3)

                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True
# Example usage
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", "2", ".", "5", ".", ".", "."],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.isValidSudoku(board))  # Output: True
# time complexity: O(1) since the board size is fixed (9x9)
# space complexity: O(1) since the sets for rows, columns, and boxes are of fixed size (9 each)