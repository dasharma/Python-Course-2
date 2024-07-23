import sys

class Link(object):
  def __init__(self,data):
    self.data=data
    self.next=None


class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.curr=None

  # Insert an element in the list
  def insert ( self, item ):
    if self.curr == None:
      self.curr = Link(item)
      self.curr.next = self.curr
    else:
      l = Link(item)
      l.next = self.curr.next
      self.curr.next = l 
      self.curr = l

  # Find the link with the given key
  def find ( self, key ):
    if self.curr == None:
      return None
    if self.curr.data == key:
      return self.curr
    cur = self.curr.next
    while cur!=self.curr:
      if cur.data == key:
        return cur
      cur = cur.next
    return None

  # Delete a link with a given key
  def delete ( self, key ):
    if self.curr == None:
      return
    if self.curr.next==self.curr and self.curr.data == key:
      self.curr = None
      return
    cur = self.curr
    while cur.next!=self.curr:
      if cur.next.data == key:
        cur.next=cur.next.next
        return
      cur = cur.next
    if cur.next.data == key:
      cur.next = cur.next.next
      self.curr = cur
      return


  # Delete the nth link starting from the Link start 
  # Return the deleted Link
  def deleteAfter ( self, start, n ):
    if start.next == start:
      self.curr = None
      return None
    cur = start
    for i in range(n-2):
      cur = cur.next
    l = cur.next
    if l == self.curr:
      self.curr = cur
    cur.next=cur.next.next
    return l

  # Return a string representation of a Circular List
  def __str__ ( self ):
    if self.curr == None:
      return '[]'
    s='['
    cur = self.curr.next
    while cur != self.curr:
      s += str(cur.data)+', '
      cur = cur.next
    s += str(cur.data)+']'
    return s

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  l = CircularList()
  for i in range(1,num_soldiers+1):
    l.insert(i)

  start = l.find(start_count)
  while(l.curr.next!=l.curr):
    deleted = l.deleteAfter(start, elim_num)
    print(deleted.data) 
    start = deleted.next
  print(l.curr.data)

if __name__ == "__main__":
  main()
