__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

print("Welcome to 2D-Vectors Calculator")

class Add2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Add2D(self.x + other.x, self.y + other.y)
    
class Sub2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Sub2D(self.x - other.x, self.y - other.y)

print("1.Add         2.Subtract")
print("3.Multiply by scale factor")
print("4.Dot product")
num=str(input("Choose an option: "))

if num=="1":
  print("Enter vectors as (x,y)")
  print("First vector")
  a1,a2=int(input("x: ")), int(input("y: "))
  print("Second vector")
  b1,b2=int(input("x: ")), int(input("y: "))
  first = Add2D(a1,a2)
  second = Add2D(b1,b2)
  result = first + second
  a=(result.x,result.y)
  print("The resultant is", a)

elif num=="2":
  print("Enter vectors as (x,y)")
  print("First vector")
  a1,a2=int(input("x: ")), int(input("y: "))
  print("Second vector")
  b1,b2=int(input("x: ")), int(input("y: "))
  first = Sub2D(a1,a2)
  second = Sub2D(b1,b2)
  result = first + second
  b=(result.x,result.y)
  print("The resultant is", b)

elif num=="3":
  a=int(input("Enter the factor: "))
  print("Enter vectors as (x,y)")
  b,c = int(input("x: ")), int(input("y: "))
  d=(a*b,a*c)
  print("The resultant is", d)

if num=="4":
  print("Enter vectors as (x,y)")
  print("First vector")
  a1,a2=int(input("x: ")), int(input("y: "))
  print("Second vector")
  b1,b2=int(input("x: ")), int(input("y: "))
  c1=a1*b1
  c2=a2*b2
  d=c1+c2
  print("The resultant is", d)