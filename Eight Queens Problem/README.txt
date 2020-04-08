Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn14.html

Eight Queens Problem ( Due 21 Oct 2019 )
The Eight Queens Problem is a fairly old problem that has been well discussed and researched. The first published reference to this problem was in a German Chess magazine in 1848 by Max Bezzel. In 1850, Franz Nauck published all 92 solutions of the problem for an 8x8 board. S. Gunther in 1874 suggested a method for finding solutions by using determinants and J.W.L. Glaisher extended this method. E. Dijkstra published a detailed description of the solution of the problem as a depth-first backtracking algorithm.

The original statement of the problem ran as follows - how can we place eight queens on a regular chess board such that no queen can capture another. It turns out there is no unique solution but 92 possible solutions of which only 12 are distinct. The 12 distinct solutions can generate all other solutions through reflections and / or rotations. Here is a table that gives the size of the board, all possible solutions, and all distinct solutions.

Size	All Solutions	Distinct Solutions
1	1	1
2	0	0
3	0	0
4	2	1
5	10	2
6	4	1
7	40	6
8	92	12
This is a classic back-tracking problem and we have discussed the solution and code in class. The code that we worked on prints only one possible solution to the problem. There are several variations to this problem and their solutions.

Prompt the user to enter the size of the board. The size of the board must be a number between 1 and 8 inclusive. Keep prompting the user to enter a number in that range, if he does not get it right. For the size of the board that the user specified generate and print all possible solutions for that size. Keep a count of the number of solutions and your last line should print the total number. Here is a possible scenario:

Enter the size of board: 4

* Q * *
* * * Q
Q * * *
* * Q *

* * Q *
Q * * *
* * * Q
* Q * *

There are 2 solutions for a 4 x 4 board.
For grading purposes, your prompt should end in a colon character then a space character (': '). Do not place any colons in any other places in any prompt or printed output. Matching the provided sample prompt will expedite grading.
The file that you will be turning in will be called Queens.py. We are looking for clean and structured design. The file will have a header of the following form:

#  File: Queens.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
If you are working with a partner both of you will be submitting the same program (from both accounts) but make sure that you have your partner's name and eid in your program. If you are working alone, then remove the two lines that has the partner's name and eid in the header.

Use the Canvas system to submit your Queens.py file. We should receive your work by 11 PM on Monday, 21 Oct 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
References
Eight Queens Problem Article in Wolfram MathWorld.
Article on Eight Queens Problem in Wikipedia Watch the animation of the recursive solution.
