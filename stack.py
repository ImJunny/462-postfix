#STACK CLASS
class Stack:
  def __init__(self):
    self.items=[]

  def isEmpty(self):
    return len(self.items)==0
  
  def top(self):
    if (not self.isEmpty()): return self.items[-1]
    else: print("no items in stack")

  def pop(self):
    if (not self.isEmpty()): return self.items.pop()
    else: print("no items to pop")

  def append(self,x): self.items.append(x)
  def size(self): return len(self.items)

  def printStack(self):
    for y in self.items:
      print(y,end="")
    print()

#GET PRECEDENCE METHOD
def prec(x):
  if (x=="*" or x=="/"):
    return 1
  if (x=="+" or x=="-"):
    return 0
  return -1

#INFIX TO POSTFIX METHOD
def infixToPostfix(input):
  operators = Stack()
  postfix = Stack()
  #for each symbol in input, place accordingly
  for x in input:
    if (x.isdigit()): postfix.append(x)

    elif (operators.size()==0 or x=="("): operators.append(x)

    elif (x==")"):
      while (operators.top()!="("):
        postfix.append(operators.pop())
      operators.pop()
    elif (prec(x) > prec(operators.top())): operators.append(x)
    else:
      while(operators.size() and prec(x) <= prec(operators.top())):
        postfix.append(operators.pop())
      operators.append(x)

  #pop remaining operators from operators to expression
  while (operators.size()):
    postfix.append(operators.pop())

  return postfix

#CALCULATE POSTFIX METHOD
def calculatePostfix(postfixStack):
  revPostfixStack = Stack()
  operands = Stack()

  #reverse stack to use top/pop accordingly
  while(postfixStack.size()>0):
    revPostfixStack.append(postfixStack.pop())
  
  while(revPostfixStack.size()>0):
    #if operand, append to operand stack
    if (revPostfixStack.top().isdigit()):
      operands.append(revPostfixStack.pop())
    #if operator, update operand stack accordingly
    else:
      newNum=0
      num1 = float(operands.pop())
      num2 = float(operands.pop())
      if (revPostfixStack.top()=="*"): newNum = num2*num1
      elif (revPostfixStack.top()=="/"): newNum = num2/num1
      elif (revPostfixStack.top()=="+"): newNum = num2+num1
      else: newNum = num2-num1
      revPostfixStack.pop()  

      operands.append(newNum)
  #return operand stack
  return operands

#MAIN
def main():
  #infix goes here
  input = "8*5*2/(1+5-3*2*(3/2)*5)"
  postfixStack = infixToPostfix(input)
  calculationStack = calculatePostfix(postfixStack)

  #print answer
  print("answer is", calculationStack.top())

if __name__=="__main__":
  main()