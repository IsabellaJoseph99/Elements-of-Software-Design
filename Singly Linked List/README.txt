Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn16.html

Singly Linked List ( Due 01 Nov 2019 )
In this assignment you will be writing helper methods for the LinkedList class that we developed and test them. The following is the outline of the code that you will be submitting. For the time being assume that the data that you are handling are integers. Later on when you use objects of other classes you will write compare functions for those classes and you can use your LinkedList class as is.

class Link (object):
  ...

class LinkedList (object):
  # get number of links 
  def get_num_links (self):
  
  # add an item at the beginning of the list
  def insert_first (self, data): 

  # add an item at the end of a list
  def insert_last (self, data): 

  # add an item in an ordered list in ascending order
  def insert_in_order (self, data): 

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):

  # Copy the contents of a list and return new list
  def copy_list (self):

  # Reverse the contents of a list and return new list
  def reverse_list (self): 

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self): 

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):

  # Return True if a list is empty or False otherwise
  def is_empty (self): 

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other): 

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()

if __name__ == "__main__":
  main()
For this assignment you may work with a partner. Both of you must read the paper on Pair Programming. .

The file that you will be turning in will be called TestLinkedList.py. The file will have a header of the following form:
#  File: TestLinkedList.py

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

Use the Canvas system to submit your TestLinkedList.py file. We should receive your work by 11 PM on Friday, 01 Nov 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
