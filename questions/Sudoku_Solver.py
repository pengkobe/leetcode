# -*- coding: utf-8 -*-
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# Empty cells are indicated by the character '.'.

# You may assume that there will be only one unique solution.

# A sudoku puzzle...

# ...and its solution numbers marked in red.
# https://leetcode.com/problems/sudoku-solver/description/


## 击败90%的答案
import copy
def solveSudoku(board):
    # 填充面板 
    def fill_board(board):
        validNums = set('123456789');
        choices = {};
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    square = {board[i // 3 * 3 + y][j // 3 * 3 + x] for y in range(3) for x in range(3)}
                    #square = {board[s][t] for s in [i,i+1,i+2] for t in [j,j+1,j+2]};
                    xrow = {board[i][s1] for s1 in range(9)};#set(board[i]);
                    yrow = {board[s2][j] for s2 in range(9)};
                    dvalues = validNums.difference(square,xrow,yrow);
                   
                    if len(dvalues) == 1:
                        board[i][j] = dvalues.pop();
                        return fill_board(board);
                    elif len(dvalues) == 0:
                        return "";
                    else:
                        choices[(i,j)] = dvalues;
        if not choices:
            return "complete";

        options = [];
        # 先尝试可选值范围最小的，最大化的优化显示结果
        x, y = min(choices, key=lambda k: len(choices[k]))
        for n in choices[(x,y)]:
            t = copy.deepcopy(board);
            t[x][y] = n;
            options.append(t);
        return options;


    # 深度优先遍历
    def dfs(board):
        stack = [board];
        while stack:
            temp = stack.pop();
            tResultList = fill_board(temp);
            if tResultList == 'complete':
                return temp;
            # 将可选答案入栈
            for t in tResultList:
                stack.append(t);
        print('dfs--end')

    newBoard =[["" for i in range(9)] for j in range(9)]
    for j in range(9):
        for i in range(9): 
            newBoard[i][j] = board[i][j];
    res = dfs(newBoard);
    # 整理返回结果
    for n,row in enumerate(res):
        board[n] = ''.join(row);

    # 为了通过 leetcode 测试，需要把这句给注释掉！
    return board;

    
print(solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]))




# import copy
# def solveSudoku(board):
#     def fill_board( board):
#         digits = set('123456789')
#         choice, best = {}, []
#         for j in range(9):
#             for i in range(9):
#                 if board[j][i] == '.':
#                     square = {board[j // 3 * 3 + y][i // 3 * 3 + x]
#                             for y in range(3) for x in range(3)}
#                     row = {board[j][x] for x in range(9)}
#                     col = {board[y][i] for y in range(9)}
#                     rest = digits.difference(square, row, col)
#                     if len(rest) == 1: # 找到唯一解
#                         board[j][i] = rest.pop()
#                         return fill_board(board)
#                     elif len(rest) == 0: # 无解
#                         return ''
#                     else:# 可选值
#                         choice[(j, i)] = rest
#         if not choice:
#             return 'complete'
#         y, x = min(choice, key=lambda k: len(choice[k]))
#         for n in choice[(y, x)]:
#             b = copy.deepcopy(board)
#             b[y][x] = n
#             best.append(b)
#         return best  

    
#     def dfs(board):
#         stack = [board]
#         while stack:
#             s = stack.pop()
#             result = fill_board(s)
#             if result == 'complete':
#                 return s
#             for r in result:
#                 stack.append(r) 

    

#     newBoard =[ ["" for i in range(9)] for j in range(9)]
    
#     for j in range(9):
#         for i in range(9): 
#             newBoard[i][j] = board[i][j];
#     print(newBoard);
#     res = dfs(newBoard)
#     for n, row in enumerate(res):
#         board[n] = ''.join(row) 
#     return board;
