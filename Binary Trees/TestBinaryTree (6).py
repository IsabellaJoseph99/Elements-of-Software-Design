#  File: TestBinaryTree.py

#  Description: Program that adds functions to determine if trees are similar, prints nodes on the same level, gets the height of the tree, and the number of nodes

#  Student Name: Isabella Joseph

#  Student UT EID: ij2799

#  Partner Name:  Kaitlyn Ng

#  Partner UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/19/19

#  Date Last Modified: 11/19/19

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

class Tree (object):
    def __init__(self):
        self.root = None

    def insert(self, val):    # copied from mitra
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lChild
                else:
                    current = current.rChild

            if (val < parent.data):
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        aNode = self.root
        bNode = pNode
        return self.is_similar_helper(aNode,bNode)

    def is_similar_helper(self, aNode, bNode):
        if aNode is None and bNode is not None:
            return False
        elif aNode is not None and bNode is None:
            return False
        elif aNode is None and bNode is None:
            return True
        else:
            if aNode.data == bNode.data:
                return self.is_similar_helper(aNode.rChild, bNode.rChild) and self.is_similar_helper(aNode.lChild, bNode.lChild) and True
            return False

    # Prints out all nodes at the given level
    def print_level (self, level):
        self.print_level_helper(self.root, level)

    # where aNode will be initialized as the root
    def print_level_helper(self, aNode, level):
        if level == 0:
            return None
        elif level == 1:
            if aNode is not None:
                print(aNode.data)
        else:
            if aNode is None:
                return
            if aNode.lChild is not None:
                self.print_level_helper(aNode.lChild, level - 1)
            if aNode.rChild is not None:
                self.print_level_helper(aNode.rChild, level - 1)

    # Returns the height of the tree
    def get_height (self):
        aNode = self.root
        return self.get_height_helper(aNode)

    # helper function that recursively gets height, use breadth first search
    def get_height_helper(self, aNode):
        if aNode is None:
            return 0
        elif aNode.lChild is None and aNode.rChild is None:
            return 0
        else:
            return 1 + max(self.get_height_helper(aNode.lChild), self.get_height_helper(aNode.rChild))

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        if self.root is None:
            return 0
        left_nodes = self.num_nodes_helper(self.root.lChild)
        right_nodes = self.num_nodes_helper(self.root.rChild)
        root_node = 1
        return left_nodes + right_nodes + root_node

    # aNode is the left child of the root
    def num_nodes_helper(self, aNode):
        if aNode is None:
            return 0
        elif aNode.lChild is None and aNode.rChild is None:
            return 1
        else:
            return self.num_nodes_helper(aNode.lChild) + self.num_nodes_helper(aNode.rChild) + 1


def main():
    # Create three trees - two are the same and the third is different
    integers = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    atree = Tree()
    for integer in integers:
        atree.insert(integer)

    # btree is the same as atree
    integers = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    btree = Tree()
    for integer in integers:
        btree.insert(integer)

    # ctree is different from atree
    integers = [50, 35, 70, 10, 40, 60, 80, 72, 2, 38, 7, 58, 65]
    ctree = Tree()
    for integer in integers:
        ctree.insert(integer)

    # Test your method is_similar()
    print(atree.is_similar(btree.root))
    print(atree.is_similar(ctree.root))
    print()

    # Print the various levels of two of the trees that are different
    atree.print_level(4)
    print()
    ctree.print_level(4)

    # Get the height of the two trees that are different
    print()
    print(btree.get_height())
    print(ctree.get_height())

    # Get the total number of nodes a binary search tree
    print()
    print(atree.num_nodes())
    print(ctree.num_nodes())
main()