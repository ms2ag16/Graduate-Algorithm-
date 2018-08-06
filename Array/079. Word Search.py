"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if self._hasEnoughCharacters(board,word):
            nrow=len(board)
            ncol=len(board[0])
            for i in range(nrow):
                for j in range(ncol):
                    if self._exist(board, i, j, nrow, ncol, word):
                        return  True
        return False




    def _exist(self,board,i,j,nrow,ncol,word):
        if len(word)==0:
            return True
        if i<0 or i>=nrow or j<0 or j>=ncol or board[i][j]!=word[0]:
            return False
        temp=board[i][j]
        board[i][j]='.'
        next_target=word[1:]
        next_result=self._exist(board,i-1,j,nrow,ncol, next_target) or self._exist(board,i+1,j,nrow,ncol, next_target) or \
                 self._exist(board, i , j-1, nrow, ncol, next_target) or  self._exist(board,i,j+1,nrow,ncol, next_target)
        board[i][j]=temp
        return next_result





    def _hasEnoughCharacters(self, board, word):
        from collections import defaultdict

        character_counts = defaultdict(int)
        for ch in word:
            character_counts[ch] += 1

        return all(sum(map(lambda line: line.count(ch), board)) >= count for ch, count in character_counts.items())
        
