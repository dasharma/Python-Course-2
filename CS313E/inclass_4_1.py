class Stack (object):

  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    if(not self.isEmpty()):
      return self.stack.pop()
    else:
      return None

  # check what item is on top of the stack without removing it
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size(self):
    return (len(self.stack))

  # a string representation of this stack. 
  def __str__(self):
    return str(self.stack)


#from example_006_stack import Stack

class queue_adapter:

   def __init__(self):

       self.stack1=Stack()

       self.stack2=Stack()


   def enqueue(self, item):
# complete this method
        while (self.stack1.size()) != 0: 
            self.stack2.push(self.stack1.pop())
            
  
        # Push item into self.s1 
        self.stack1.push(item) 
  
        # Push everything back to s1 
        while (self.stack2.size()) != 0: 
            self.stack1.push(self.stack2.pop()) 
            
 

   #def dequeue(self):
# complete this method
        # Return top of self.stack1 
       # x = self.stack1.pop() 
         
        #return x

    def dequeue(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            return None

        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()
###############################
#                             #
#   Example run of a stack    #
#                             #
###############################

def main():

  my_stack = Stack()

  # Push 10
  my_stack.push(10)
  print(my_stack)

  # Push 18
  my_stack.push(18)
  print(my_stack)


  # Push 1024
  my_stack.push(1024)
  print(my_stack)


  # pop() 
  print("pop()  ", my_stack.pop())


  # peek()
  print("peak()  ", my_stack.peek())


  # isEmpty()
  print("isEmpty()   ", my_stack.isEmpty())


  print("pop()  ", my_stack.pop())
  print("pop()  ", my_stack.pop())
  print("pop()  ", my_stack.pop())
  print("isEmpty()   ", my_stack.isEmpty())


#if __name__ == '__main__':
    #main()
stack1 = Stack()
stack1.push(10)
stack1.push(14)
stack1.push(9)
stack1.push(17)
print(stack1)


q = queue_adapter()
q.stack1 = stack1
q.enqueue(6)

q.dequeue()
print(q.stack1)
