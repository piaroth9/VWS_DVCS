#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Tic Tac Toe Game - Clean Code Development
"""

def display_board(board):
    """
    Display the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Check if the specified player has won the game.
    """
    for i in range(3):
        # Check horizontal and vertical lines
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def make_move(board, row, col, player):
    """
    Make a move on the board for the specified player.
    """
    if board[row][col] == " ":
        board[row][col] = player
        return True

    print("Invalid move! Position already taken. Try again.")
    return False

def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        display_board(board)
        row = int(input(f"Player {current_player}, choose row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, choose column (1-3): ")) - 1

        if make_move(board, row, col, current_player):
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif all(cell != " " for row in board for cell in row):
                display_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()

