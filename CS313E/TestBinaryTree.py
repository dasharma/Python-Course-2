

#  File: TestBinaryTree.py

#  Description: finish the get level, range, sum of leaves, and left view codes
#  using iterative approaches using stacks and recursion approaches using helper functions.

#  Student Name: Viren Govin

#  Student UT EID: vmg984

#  Partner Name: Diya Sharma

#  Partner UT EID: das5954

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 3/22/2023

#  Date Last Modified: 3/23/2023


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        max = 0
        min = 99999999
        stack = []
        stack.append(self.root)
        #grab top value from stack
        while len(stack)>0:
            node = stack.pop()
            if node.data > max:
                max = node.data
            if node.data < min:
                min = node.data
            
            if node.lChild !=None:
                stack.append(node.lChild)
            if node.rChild !=None:
                stack.append(node.rChild)
        return max - min

    #helper recursion function for get_level.
    #Takes node, level, current level, and list as paramaters  
    def recur_level(self, node, level, curr_level, l):
        
        if level == curr_level and node != None:
            l.append(node)
        else:
            if node.lChild != None:
                self.recur_level(node.lChild, level, curr_level+1,l) 
            if node.rChild != None:
                self.recur_level(node.rChild, level, curr_level+1,l)
            
        
        #nodes.append(self.recur_level(level, curr_level-1, nodes))

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level ):
        if self.root == None:
            return []
        l = []      
        self.recur_level(self.root, level, 0, l)
        return l

    def left_side_view(self):
        output = []
        for i in range(self.get_height()):
            output.append(self.get_level(i)[0].data)
        return output

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):

        #push root node onto stack
        sum = 0
        stack = []
        stack.append(self.root)

        while len(stack) > 0:
            #node is equal to the top of the stack
            node = stack.pop()
            if node.lChild == None and node.rChild == None:
                sum = sum + node.data
            else:
                if node.lChild != None:
                    stack.append(node.lChild)
                if node.rChild != None:
                    stack.append(node.rChild)
        return sum



def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()



