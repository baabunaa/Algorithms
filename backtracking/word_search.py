# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def find(board, i, j, word, index):
            if len(word) == index: return True
            if j < 0 or j >= len(board[0]) or i < 0 or i >= len(board): return False
            if board[i][j] != word[index]: return False
            tmp, board[i][j] = board[i][j], None
            index += 1
            left = find(board, i, j-1, word, index)
            right = find(board, i, j+1, word, index)
            up = find(board, i-1, j, word, index)
            down = find(board, i+1, j, word, index)
            board[i][j] = tmp
            return left or right or up or down 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if find(board, i, j, word, 0): return True
        return False
