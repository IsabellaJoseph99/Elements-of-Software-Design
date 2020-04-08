Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn12.html

Magic Squares through Permutation ( Due 14 Oct 2019 )
In a previous assignment we worked on an algorithm that produced magic squares of odd order. We avoided generating magic squares of even order because the algorithm for generating them is more complicated.

Here is a very famous magic square that is featured in the painting Melancholia by Albrecht Durer.

16   3   2  13
 5  10  11   8
 9   6   7  12
 4  15  14   1
In this assignment you will generate onlyTEN magic squares of order 4 through permutation. The process is straight forward but time consuming. Here are the steps:

Create a 1-D list of integers 1 through 16.
Permute this list of integers.
For each permutation convert the 1-D list into a 2-D list that is 4 x 4.
Check if that 2-D list is a magic square. If it is, then print it out.
Stop when you have gone through all the permutations.
The magic constant is given by n * (n2 + 1) / 2, where n is the dimension of the magic square. For a 4 x 4 magic square the constant is 34.

In this program there is no user input. You may reuse any code that you have written for the first assignment. To save space you may print out your magic squares as 1-D list of numbers. Your output will look as follows:

[1, 2, 15, 16, 12, 14, 3, 5, 13, 7, 10, 4, 8, 11, 6, 9] 
[1, 2, 15, 16, 13, 14, 3, 4, 12, 7, 10, 5, 8, 11, 6, 9]
[1, 2, 16, 15, 13, 14, 4, 3, 12, 7, 9, 6, 8, 11, 5, 10]
[1, 3, 14, 16, 10, 13, 4, 7, 15, 6, 11, 2, 8, 12, 5, 9]
[1, 3, 14, 16, 12, 13, 4, 5, 15, 8, 9, 2, 6, 10, 7, 11]
[1, 3, 14, 16, 15, 13, 4, 2, 10, 6, 11, 7, 8, 12, 5, 9]
[1, 3, 14, 16, 15, 13, 4, 2, 12, 8, 9, 5, 6, 10, 7, 11]
[1, 3, 16, 14, 8, 15, 2, 9, 13, 6, 11, 4, 12, 10, 5, 7]
[1, 3, 16, 14, 12, 15, 2, 5, 13, 10, 7, 4, 8, 6, 9, 11]
[1, 3, 16, 14, 13, 15, 2, 4, 12, 10, 7, 5, 8, 6, 9, 11]
There should be 10 magic squares of order 4.
You must optimize your code so that it does not go through all the permuations. For example, if the first row does not add to the magic constant 34 stop that permutation and go to the next one. If the second row does not add to the magic constant then stop that permutation and go to the next one. And similarly for the sum of the third row.

For this assignment you may work with a partner. Both of you must read the paper on Pair Programming. .

The file that you will be uploading will be called EvenMagicSquare.py. We are looking for clean and structured design. The file will have a header of the following form:

#  File: EvenMagicSquare.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
If you are working with a partner both of you will be submitting the same program but make sure that you have your partner's name and eid in your program. If you are working alone, then remove the two lines that has the partner's name and eid in the header.

Use the Canvas system to submit your EvenMagicSquare.py file. We should receive your work by 11 PM on Monday, 14 Oct 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
References
Even Order Magic Square
Durer's Magic Square
