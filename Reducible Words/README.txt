Details taken from assignment link: https://www.cs.utexas.edu/users/mitra/csFall2019/cs313/assgn/assgn15.html

Reducible Words ( Due 28 Oct 2019 )
What is the longest English word that remains a valid English word as you remove one letter at a time from the word?

The letters can be removed anywhere from the word one at a time but you may not rearrange the remaining letters to form a valid word. Every time you remove a letter the remaining letters form a valid English word. Eventually you will end up with a single letter and that single letter must also be a valid English word. A valid English word is one that is found in the Oxford English Dictionary or the Webster's Dictionary.

For want of a better term we will call such words reducible words. Here are two examples of reducible words:

1: sprite. If you remove the r you get spite. Remove the e and you get spit. Remove the s and you get pit. Remove the p and you get it. Remove the t and you get i or I which is a valid English word.

2: string. Take away the r and you have sting. Take away the t and you have sing. Take away the g and you have sin. Take away the s and you have in. Take away the n and you have i or I which is a valid English word.

So all reducible words will reduce to one of three letters - a, i, and o. We will not accept any other letter as the final one letter word.

There is no official word list in an electronic form that we can use. We will use a curated word list file called words.txt. All the words are in lower case and are two letters or more in length. This word list will do as our input file.

Your output will be the longest word that is reducible. If there are more than one word having that maximum length, then you will print each word in alphabetical order on a line by itself.

Here is the outline of the code. The algorithm has been discussed in class. You may always add more helper functions as needed.

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
	hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size (s, const):

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible (s, hash_table, hash_memo):

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):

def main():
  # create an empty word_list

  # open the file words.txt

  # read words from words.txt and append to word_list

  # close file words.txt

  # find length of word_list

  # determine prime number N that is greater than twice
  # the length of the word_list

  # create and empty hash_list

  # populate the hash_list with N blank strings

  # hash each word in word_list into hash_list
  # for collisions use double hashing 

  # create an empty hash_memo

  # populate the hash_memo with M blank strings

  # create and empty list reducible_words

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words

  # find words of the maximum length in reducible_words

  # print the words of maximum length in alphabetical order
  # one word per line

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
For this assignment you may work with a partner. Both of you must read the paper on Pair Programming. .

The file that you will be uploading will be called Reducible.py. We are looking for clean and structured design. The file will have a header of the following form:

#  File: Reducible.py

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

Use the Canvas system to submit your Reducible.py file. We should receive your work by 11 PM on Monday, 28 Oct 2019. There will be substantial penalties if you do not adhere to the guidelines. Remember Python is case sensitive. The name of your file must match exactly what we have specified.

Your Python program should have the proper header.
Your code must run before submission.
You should be submitting your file through the web based Canvas program. We will not accept files e-mailed to us.
Here is the Grading Criteria.
