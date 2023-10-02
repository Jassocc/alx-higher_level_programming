#!/usr/bin/python3
"""
Module 10
N queens puzzle challenge
"""

import sys

def is_safe(board, row, colu):
    """
    checks for places its safe
    """
    for a in range(row):
        if board[a][colu] == 1:
            return False
        if colu - a >= 0 and board[row-a][colu-a] == 1:
            return False
        if colu + a < len(board) and board[row-a][colu+a] == 1:
            return False
    return True

def solve_nqueens_util(board, row):
    """
    solves the puzzle
    """
    solutions = []
    if row == len(board):
        queen_pos = [[i, row.index(1)] for i, row in enumerate(board)]
        queen_pos.sort()
        solutions.append(queen_pos)
        return solutions
    for colu in range(len(board)):
        if is_safe(board, row, colu):
            board[row][colu] = 1
            solutions += solve_nqueens_util(board, row + 1)
            board[row][colu] = 0
    return solutions

def solve_nqueens(n):
    """
    solve for nqueens
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = solve_nqueens_util(board, 0)
    solutions.sort()
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)
