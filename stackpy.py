class stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    return self.items.append(item)
  
  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)

  def pop(self):
      return (remove self.items[-1])
      


s = stack()
s.append(5)
while(True):
    print("enter 1 for push")
    print("enter 2 for pop")
    print("enter 3 for top item")
    a=int(input("enter choice"))
    if(a==1):
        b=int(input("Enter no. you want to push"))
        s.push(b)
        break
    elif(a==2):
        print("size is",s.size())
        if s.size()==0:
            print("no items to pop")
        else:
            print(s.pop())
            
    
print("s.peek())

print(s.size())
print(s.isEmpty())
