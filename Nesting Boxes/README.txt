Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn13.html

Nesting Boxes ( Due 18 Oct 2019 )
Imagine a room full of boxes. Each box has a length, width, and height. Since the boxes can be rotated those terms are inter- changeable. The dimensions are integral values in a consistent system of units. The boxes have rectangular surfaces and can be nested inside each other. A box can nest inside another box if all its dimensions are strictly less than the corresponding dimensions of the other. You may only nest a box such that the corresponding surfaces are parallel to each other. A box may not be nested along the diagonal. You cannot also put two or more boxes side by side inside another box.

The list of boxes is given in a file called boxes.txt. The first line gives the number of boxes n. The next n lines gives a set of three integers separated by one or more spaces. These integers represent the 3 dimensions of a box. Since you can rotate the boxes, the order of the dimensions does not matter. It may be to your advantage to sort the dimensions in ascending order.

The output of your code will be the largest subset of boxes that nest inside each other starting with the inner most box to the outer most box. There should be one line for each box.

Largest Subset of Nesting Boxes
(2, 2, 3)
(3, 4, 4)
(5, 5, 6)
(6, 7, 9)
If there is two or more subsets of equal lengths that qualify as being the largest subset, then print all the largest qualifying subsets with a one line space between each subset. The minimum number of boxes that qualify as nesting is 2. If there are no boxes that nest in another, then write "No Nesting Boxes" instead of "Largest Subset of Nesting Boxes".

For the data set that has been given to you, here is the solution set.

For this assignment you may work with a partner. Both of you must read the paper on Pair Programming. .

The file that you will be turning in will be called Boxes.py. We are looking for clean and structured design. The file will have a header of the following form:

#  File: Boxes.py

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

Use the Canvas system to submit your Boxes.py file. We should receive your work by 11 PM on Friday, 18 Oct 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
