from typing import *
def search(board, word, i, j, k, found):
    p = [1, -1, 0, 0]
    q = [0, 0, 1, -1]

    if found[0]:
        return

    if k == len(word):
        found[0] = True
        return

    if(i<0 or j<0 or i >= len(board) or j >= len(board[0])):
        return

    if board[i][j] != word[k]:
        return

    for x in range(4):
        temp = board[i][j]
        board[i][j] = "$"
        search(board, word, p[x] + i, q[x] + j, k+1, found)
        board[i][j] = temp

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if found[0]: return found[0]
                search(board, word, i, j, 0, found)
        return found[0]
