import turtle
from turtle import *
t = Turtle()
t.speed(1000)
def square1():
    for i in range (4):
     t.forward(100)
     t.left(90)
#square1()

def square():
 for i in range (60):
     for i in range (4):
        t.forward(100)
        t.left(90)
     
     t.right(5)

#square()

def triangle():
 for i in range (60):
   for i in range (4):
     t.forward(300)
     t.left(90)

   t.right(5)

#traingle()

def traingle1():
  for i in range (60):
    for i in range (4):
      t.forward(150)
      t.left(90)
    t.right(5)

#traingle1()

length = 100
for i in range (20):
  t.forward(length)
  t.left(90)
  length =+ 25


    