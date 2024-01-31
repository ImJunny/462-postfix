#CQUEUE CLASS
class CQueue:
  def __init__(self,size):
    self.size = size
    self.queue = [None]*size
    self.front = -1
    self.rear = -1

  def enqueue(self,item):
    if (self.front==0 and self.rear==self.size-1) or ((self.rear+1)%self.size==self.front): print("queue is full")
    else:
      self.rear+=1
      if self.rear==self.size: self.rear=0
      if self.front==-1: self.front=0
      self.queue[self.rear] = item

  def dequeue(self):
    if self.front==-1:
      print("queue is empty")
      return
    if self.front==self.rear: 
      self.front=-1
      self.rear=-1
    else:
      self.front+=1
      if (self.front==self.size): self.front=0
  
  def printQueue(self):
    print(self.queue)

#MAIN METHOD
def main():
  CircularQ = CQueue(5)
  CircularQ.enqueue(1)
  CircularQ.enqueue(2)
  CircularQ.enqueue(3)
  CircularQ.enqueue(4)
  CircularQ.enqueue(5)
  CircularQ.dequeue()
  CircularQ.enqueue(10)
  CircularQ.enqueue(10)
  CircularQ.enqueue(10)
  CircularQ.dequeue()
  CircularQ.dequeue()
  CircularQ.dequeue()
  CircularQ.dequeue()
  CircularQ.dequeue()
  CircularQ.dequeue()
  CircularQ.enqueue(20)

  CircularQ.printQueue()

if __name__=="__main__":
  main()