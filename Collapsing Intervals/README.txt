Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn2.html

Collapsing Intervals (Due 09 Sep 2019)
An interval on the number line is denoted by a pair of values like so: (3, 8). Our intervals are closed. So this interval represents all numbers between 3 and 8 inclusive. The first number is always going to be strictly less than the second number. Normally in mathematics we represent a closed interval with square brackets. But in our program we will represent an interval by means of a tuple and tuples in Python are represented with parentheses.

If we have two intervals like (7, 12) and (4, 9), they overlap. We can collapse overlapping intervals into a single interval (4, 12). But the following two intervals (-10, -2) and (1, 5) are non-intersecting intervals and cannot be collapsed.

The aim in this assignment is take a set of intervals and collapse all the overlapping intervals and print the smallest set of non-intersecting intervals in ascending order of the lower end of the interval.

The input data will be in a file called intervals.txt. There will be one or more lines of data in the file. Each line will have two integer numbers denoting an interval. The first number will be strictly less than the second number. Assume that the data file is correct.

You will read in each pair of numbers and create a tuple out of them. You will store the tuples in a list. After you have read all the intervals and the list of tuples is complete you will sort the list. Then you will go through the list systematically and replace each pair of overlapping tuples with a single tuple. When you are done you should print out the list of non-intersecting tuples with one tuple per line. The list should be in ascending order of the lower end of the tuples.

For the data file that is given with this problem statement, your output will have the following format:

Non-intersecting Intervals:
(-25, -14)
(-10, -3)
(2, 6)
(12, 18)
(22, 30)
Extra Credit (10 points): We will give you extra credit if you can figure out how to print the non-intersecting intervals in increasing order of the size of the intervals. If two intervals are of the same size then you should print the two intervals in ascending order of their lower ends. So the extra credit output will have the following format:

Non-intersecting Intervals:
(-25, -14)
(-10, -3)
(2, 6)
(12, 18)
(22, 30)

Non-intersecting Intervals in order of size:
(2, 6)
(12, 18)
(-10, -3)
(22, 30)
(-25, -14)
For this assignment you may work with a partner. Both of you must read the paper on Pair Programming.

The file that you will be turning in will be called Intervals.py. The file will have a header of the following form:

#  File: Intervals.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
If you are working with a partner both of you will be submitting the same copy of the program but make sure that you have your partner's name and EID in your program. If you are working alone, then remove the two lines that has the partner's name and eid in the header.

Use the Canvas program to submit your Intervals.py file. We should receive your work by 11 PM on Monday, 09 Sep 2019. There will be substantial penalties if you do not adhere to the guidelines.

Your Python program should have the header with the proper documentation.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
