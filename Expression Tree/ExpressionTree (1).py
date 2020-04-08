#  File: ExpressionTree.py

#  Description: A program that evaluates an expression, and gives the prefix and postfix notation

#  Student's Name: Isabella Joseph

#  Student's UT EID: ij2799

#  Partner's Name: Kaitlyn Ng

#  Partner's UT EID: kn8685

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 11/13/2019

#  Date Last Modified: 11/14/2019

class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def isEmpty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def __str__(self):
        return str(self.stack)

class Node (object):
    def __init__(self,data):
        self.data = data
        self.lChild = None
        self.rChild = None

    # def __str__(self):
    #     return str(self.lChild), str(self.rChild)

class Tree (object):
    def __init__ (self):
        self.root = None


    #creates an expression tree

    def create_tree (self, expr):
        operators = ['+', '-', '*', '/', '//', '%', '**']
        tokens = expr.split()
        self.root = Node(None)
        root_node = self.root
        current_node = root_node
        stack = Stack()
        for item in tokens:
            if item == "(":
                current_node.lChild = Node(None)
                stack.push(current_node)
                current_node = current_node.lChild
            if item in operators:
                current_node.data = item
                stack.push(current_node)
                current_node.rChild = Node(None)
                current_node = current_node.rChild
            if item not in operators and item != ")" and item != "(":
                current_node.data = item
                current_node = stack.pop()
            if item == ")":
                if not stack.isEmpty():
                    current_node = stack.pop()

    #calculates the value
    def operate(self, oper1, oper2, token):
        if (token == '+'):
            return oper1 + oper2
        elif (token == '-'):
            return oper1 - oper2
        elif (token == '*'):
            return oper1 * oper2
        elif (token == '/'):
            return oper1 / oper2
        elif (token == '//'):
            return oper1 // oper2
        elif (token == '%'):
            return oper1 % oper2
        elif (token == '**'):
            return oper1 ** oper2

    # recursively calculates an expression tree
    def evaluate (self, aNode):
        # fxnStack = Stack()
        operators = ['+', '-', '*', '/', '//', '%', '**']

        current = aNode

        if current != None:

            if current.rChild is None or current.lChild is None:
                return float(current.data)

            else:
                return self.operate(self.evaluate(current.lChild), self.evaluate(current.rChild), current.data)


    # reads tree in prefix notation
    def pre_order(self, aNode):

        if (aNode != None):

            if aNode.rChild is None and aNode.lChild is None:
                return str(aNode.data)

            else:
                return (str(aNode.data)+" "+str(self.pre_order(aNode.lChild))+" "+str(self.pre_order(aNode.rChild)))

    # reads tree in postfix notation
    def post_order(self, aNode):
        if (aNode != None):

            if aNode.rChild is None and aNode.lChild is None:
                return str(aNode.data)

            else:
                return (str(self.post_order(aNode.lChild)) + " " + str(self.post_order(aNode.rChild)) + " " + str(aNode.data))

def main():


    in_file = open("expression.txt", 'r')
    for line in in_file:
        expr = line

    tree = Tree()

    tree.create_tree(expr)


    print(expr + " = " + str(tree.evaluate(tree.root)))
    print()
    print("Prefix Expression: "+str(tree.pre_order(tree.root)))
    print()
    print("Postfix Expression: " + str(tree.post_order(tree.root)))

main()