#  File: Queens.py

#  Description: Program that generates solutions for a nxn board.

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name: Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 502505

#  Date Created: 10/18/19

#  Date Last Modified: 10/19/19

class Queens(object):
  # initialize the board
  def __init__(self, n=8):
    self.board = []
    self.n = n
    self.counter = 0
    for i in range(self.n):
      row = []
      for j in range(self.n):
        row.append('*')
      self.board.append(row)

  # print the board
  def print_board(self):
    if self.n == 2 or self.n == 3:
      self.counter == 0

    for i in range(self.n):
      for j in range(self.n):
        print(self.board[i][j], end=' ')
      print()
    print()

  # check if no queen captures another
  def is_valid(self, row, col):
    for i in range(self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range(self.n):
      for j in range(self.n):
        row_diff = abs(row - i)
        col_diff = abs(col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve(self, col):
    if (col == self.n):
      self.counter += 1
      self.print_board()
      return True
    else:
      for i in range(self.n):
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          self.recursive_solve(col + 1)
          # return True
          self.board[i][col] = '*'
      return False

  # if the problem has a solution print the board
  def solve(self):
    self.recursive_solve(0)
    print('There are '  + str(self.counter) + ' solutions for a ' + str(self.n) + ' x ' + str(self.n) + ' board.')

def main():
    # prompt user to input a number between 1 and 8
    user_input = 0
    while user_input < 1 or user_input > 8:
        user_input = int(input('Enter the size of the board: '))
        print()

    game = Queens(user_input)

    # place the queens on the board
    game.solve()

main()
