#  File: BST_Cipher.py

#  Description: Program that encrypts and decrypts strings given a key

#  Student Name: Kaitlyn Ng

#  Student UT EID: kn8685

#  Partner Name: Isabella Joseph

#  Partner UT EID: ij2799

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/15/19

#  Date Last Modified: 11/17/19


class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        lower_alpha = list('abcdefghijklmnopqrstuvwxyz ')
        chars = list(encrypt_str)
        for char in chars:
            if char in lower_alpha:
                self.insert(char)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        # if the character is a space, insert it all the way to the left in the tree
        # fix where the space is inserting
        new_node = Node(ch)
        if ch == ' ':
            if self.root is None:
                self.root = new_node
            else:
                current = self.root
                while current.lChild is not None:
                    current = current.lChild
                # reaches the leftmost spot where space should be inserted
                # only inserts a space one time
                if current.data != ' ':
                    current.lChild = new_node
            return

        else:
            char_value = ord(ch)

            if self.root is None:
                self.root = new_node
            else:
                current = self.root
                parent = self.root
                while current is not None:
                    parent = current
                    if char_value < ord(current.data):
                        current = current.lChild
                    elif char_value > ord(current.data):
                        current = current.rChild
                    # do not insert if the letter is already in the tree
                    else:
                        return
                if char_value < ord(parent.data):
                    parent.lChild = new_node
                elif char_value > ord(parent.data):
                    parent.rChild = new_node

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        s = ''
        if ch == ' ':
            char_value = -1
        else:
            char_value = ord(ch)
        current = self.root
        while (current is not None) and current.data != ch:
            if char_value < ord(current.data):
                s += '<'
                current = current.lChild
            elif char_value > ord(current.data):
                s += '>'
                current = current.rChild
        if self.root.data == ch:
            s += '*'
        s += '!'
        return s

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        decrypt_key = st.lower()
        symbols = list('<>')
        current = self.root
        for char in decrypt_key:
            if char in symbols:
                if char == '*':
                    return self.root.data
                elif char == '<':
                    if current.lChild is not None:
                        current = current.lChild
                elif char == '>':
                    if current.rChild is not None:
                        current = current.rChild
        return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        encrypt_key = st.lower()
        lower_alpha = list('abcdefghijklmnopqrstuvwxyz ')
        encrypt_string = ''
        for char in encrypt_key:
            if char in lower_alpha:
                encrypt_string += self.search(char)
        encrypt_string = encrypt_string[:-1]
        return encrypt_string


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        decrypt_list = st.split('!')
        s = ''
        for char in decrypt_list:
            s += self.traverse(char)
        return s


def main():
    encrypt_key = input('Enter encryption key: ')
    newTree = Tree(encrypt_key)
    encrypt_str = input('Enter string to be encrypted: ')
    print('Encrypted string:', newTree.encrypt(encrypt_str))
    decrypt_str = input('Enter string to be decrypted: ')
    print('Decrypted string:', newTree.decrypt(decrypt_str))
main()