#  File: ExpressionTree.py

#  Description: Create an expression tree, evaluate the expression tree, and then traverse it through the postfix and prefix methods.

#  Student Name: Viren Govin

#  Student UT EID: vmg894

#  Partner Name: Diya Sharma

#  Partner UT EID: das5954

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 3/20/2023

#  Date Last Modified: 3/20/2023

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        tokens = expr.split()
        stack = Stack()
        self.root = Node()
        current = self.root
        for token in tokens:
            if token == '(':
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            #operator
            elif token in operators:
                current.data = token
                current.rChild = Node()
                stack.push(current)
                current = current.rChild
            elif token == ')':
                current = stack.pop()
            #operand
            else:
                #convert operand to int
                if float(token).is_integer():
                    current.data = int(token)
                #convert operand to float if not int
                else:
                    current.data = float(token)
                current = stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode.data in operators:
            
            left_value = self.evaluate(aNode.lChild)
            right_value = self.evaluate(aNode.rChild)
            if aNode.data == '+':
                return float(left_value + right_value)
            elif aNode.data == '-':
                return float(left_value - right_value)
            elif aNode.data == '*':
                return float(left_value * right_value)
            elif aNode.data == '/':
                return float(left_value / right_value)
            elif aNode.data == '//':
                return float(left_value // right_value)
            elif aNode.data == '%':
                return float(left_value % right_value)
            elif aNode.data == '**':
                return float(left_value ** right_value)
            else:
                return aNode.data
        return aNode.data
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if aNode is None:
            return ''
        elif aNode.data not in operators:
            return str(aNode.data)+ ' '
        else:
            return str(aNode.data) + ' ' + self.pre_order(aNode.lChild) + self.pre_order(aNode.rChild)
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode is None:
            return ''
        elif aNode.data not in operators:
            return str(aNode.data) + ' '
        else:
            return self.post_order(aNode.lChild) + self.post_order(aNode.rChild) + str(aNode.data) + ' '
# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
