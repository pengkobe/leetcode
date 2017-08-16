# -*- coding: utf-8 -*-

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    def isValid(row):
        map =[];
        for r in row:
            if r in map:
                return False;
            else:
                if r != ".":
                    map.append(r);
        return True;

    ret = True;
    for i in board: # 验证行
        ret = isValid(board[i]);
        if ret:
            col = [c[i] for c in board];
            ret = isValid(col); # 验证列
            if not ret:
                return False
        else:
            return False;

    for m in [0,3,6]:
        for n in [0,3,6]:
            square = [board[s][t] for s in [i,n+1,n+2] for t in [m,m+1,m+2]];
            ret = isValid(square);
            if not ret:
                return False