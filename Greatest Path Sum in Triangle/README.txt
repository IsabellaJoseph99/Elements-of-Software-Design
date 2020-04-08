Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn24.html

Greatest Path Sum in Triangle (due 09 Dec 2019)
This assignment is a variation of a problem from Project Euler. You are required to find the greatest path sum starting at the top of the triangle and moving only to adjacent numbers on the row below.

   3
  7 4
 2 4 6
8 5 9 3
In the above triangle, the maximum path sum is 3 + 7 + 4 + 9 = 23.
You will read your input from the file triangle.txt . The first line indicates n the number of rows in the triangle. This will be followed by n lines of data. Each line of data will have only positive integers greater than 0. The first line of data in the triangle will have one number, the second line in the triangle will have two numbers and so on. The nth line will have n integers.

You will apply four different approaches to problem solving to this single problem - exhaustive search, greedy, divide and conquer (recursive), and dynamic programming. Here is the outline of the code:

import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
  return

# returns the greatest path sum using greedy approach
def greedy (grid):
  return

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
  return

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  return 

def main ():
  # read triangular grid from file

  ti = time.time()
  # output greates path from exhaustive search
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search

  ti = time.time()
  # output greates path from greedy approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach

  ti = time.time()
  # output greates path from divide-and-conquer approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach

  ti = time.time()
  # output greates path from dynamic programming 
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()
You can always add more helper functions as needed.
You will have these lines of output:

The greatest path sum through exhaustive search is 23.
The time taken for exhaustive search is x seconds.

The greatest path sum through greedy search is 23.
The time taken for greedy approach is x seconds.

The greatest path sum through recursive search is 23.
The time taken for recursive search is x seconds.

The greatest path sum through dynamic programming is 23.
The time taken for dynamic programming is x seconds.
Most likely the maximum path that you will get from exhaustive search, recursive search, and dynamic programming will be the same. Whereas the result from the greedy search will be less.
The file that you will be submitting will be called Triangle.py. We will be looking for good documentation, descriptive variable names, clean logical structure, and adherence to the coding conventions discussed in class.

You may work with a partner on this assignment. Both of you must read the paper on Pair Programming and abide by the ground rules as stated in that paper. The file will have a header of the following form:

#  File: Triangle.py

#  Description:

#  Student's Name:

#  Student's UT EID:

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
If you are working with a partner both of you will be submitting your program (from both accounts) but make sure that you have your partner's name and eid in your program. If you are working alone, then remove the two lines that has the partner's name and eid in the header.
Use the Canvas system to submit your Triangle.py file. We should receive your work by 11 PM on Monday, 09 Dec 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
