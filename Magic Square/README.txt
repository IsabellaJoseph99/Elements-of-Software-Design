Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn1.html

Magic Square ( Due 06 Sep 2019 )
A n x n matrix that is filled with the numbers 1, 2, 3, ..., n² is a magic square if the sum of the elements in each row, in each column, and in the two diagonals is the same value.

Implement the following algorithm to construct the magic n-by-n squares. This algorithm works only if n is odd.

Place a 1 in the middle of the bottom row.
After k has been placed in the (i, j) square, place k+1 into the square to the right and down, wrapping around the borders.
However, if the square to the right and down has already been filled, or if you are in the lower right corner, then you must move to the square straight up (from the last square that you were on) instead.
The skeleton of your program will be as follows. In order for you to receive full credit, your functions must match the specifications given here. In particular, return types and values must match, and you should only include print statements when specified.


# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):

# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):

def main():
  # Prompt the user to enter an odd number 1 or greater

  # Check the user input

  # Create the magic square

  # Print the magic square

  # Verify that it is a magic square

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
In your function main() you will prompt the user to enter an odd number. You must check that the input is a positive odd number greater than or equal to 1. If it is not, you will prompt the user to re-enter the number and check again and again.

Then you will create a 2-D list representing the Magic Square. You will then print out the magic square in a neat format by calling the function print_square(). In the function print_square() you MUST use print with formatting.

You will then call the function check_square(). This function checks that the sum of all the rows have the same value. It checks that the sum of all the columns have the same value. It sums the two main diagonals and checks that they have the same value. For a magic square of size n, the sum is n * (n2 + 1) / 2.

This is a sample of what the program will output:

Please enter an odd number: 5

Here is a 5 x 5 magic square:

11  18  25   2   9
10  12  19  21   3
 4   6  13  20  22
23   5   7  14  16
17  24   1   8  15

This is a magic square and the canonical sum is 65
If on the other hand the function check_square() determined that it was not a magic square, then the above line will read:
This is not a magic square
The file that you will be turning in will be called MagicSquare.py. We will be looking for good documentation, descriptive variable names, clean logical structure, and adherence to the coding conventions discussed in class. You may work with a partner on this assignment. Both of you must read the paper on Pair Programming and abide by the ground rules as stated in that paper. The file will have a header of the following form:

#  File: MagicSquare.py

#  Description:

#  Student's Name:

#  Student's UT EID:
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
If you are working with a partner then both of you will submit the same code. In the header make sure that you have your name and your partner's name. If you are working alone then remove the fields that has the partner's name and EID.
Use the Canvas system to submit your MagicSquare.py file. We should receive your work by 11 PM on Friday, 06 Sep 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
References
Magic Square Article in Wolfram MathWorld
Article on Magic Square in Wikipedia
