import turtle as t
import random
print(t.heading())
t.speed(0)
#body
t.color("brown")
t.penup()
t.goto(-130,80)
t.right(90)
t.pendown()
t.begin_fill()
t.forward(130)
for i in range(180):
    t.forward(2)
    t.left(1)
t.forward(130)
for i in range(45):
    t.forward(8)
    t.left(4)
t.end_fill()
t.left(180)

##bottom legs
t.penup()
t.goto(-120,-100)
t.color("green")
t.begin_fill()
t.pendown()
t.left(135)
t.forward(60)
t.speed(0)
for i in range(180):
  t.forward(0.5)
  t.left(1)
t.forward(57)
t.end_fill()

t.penup()
t.goto(90,-98)
t.pendown()
t.right(90)
t.begin_fill()
t.forward(60)
t.speed(0)
for i in range(180):
  t.forward(0.5)
  t.right(1)
t.forward(59)
t.penup()
t.right(45)
t.end_fill()

#top legs
t.speed(0)
t.color("lime")
##top right leg
t.goto(52,175)
#110,175

t.right(70)
t.pendown()
t.begin_fill()
t.speed(0)
for i in range(35):
    t.forward(4)
    t.right(1)
t.left(150)
for i in range(15):
    t.forward(2)
    t.left(1)
for i in range(10):
    t.forward(9)
    t.left(2)
for i in range(3):
    t.forward(10)
    t.left(10)
for i in range(10):
    t.left(5)
    t.forward(2)
for i in range(17):
    t.left(1)
    t.forward(2)
t.left(3)
t.hideturtle()
t.end_fill()
t.penup()
##top left leg
#180 degrees
t.showturtle()
#-80,175
t.goto(-82,175)
t.left(180)

t.left(70)

t.pendown()
t.begin_fill()
t.speed(0)
for i in range(35):
    t.forward(4)
    t.left(1)
t.right(150)
for i in range(15):
    t.forward(2)
    t.right(1)
for i in range(10):
    t.forward(9)
    t.right(2)
for i in range(3):
    t.forward(10)
    t.right(10)
for i in range(10):
    t.right(5)
    t.forward(2)
for i in range(17):
    t.right(1)
    t.forward(2)
t.right(3)
t.hideturtle()
t.end_fill()

t.penup()
t.left(180)
#facing up

#turtle head
#52,175
#-82,175
t.goto(-40,195)
t.pendown()
t.color("green")   #middle is -15,175
t.begin_fill()           #40 units long head
t.right(10)
t.forward(20)
t.left(30)
for i in range(20):
    t.forward(2.5)
    t.right(1)
for i in range(180):
    t.right(1)
    t.forward(0.56)
for i in range(20):
    t.forward(2.5)
    t.right(1)
t.left(30)
t.forward(20)
t.right(10)

#t.penup()
#t.goto(10,195)
#t.pendown()
#t.left(180)
#t.left(10)
#t.forward(20)
#t.right(30)
#for i in range(20):
#    t.forward(3)
#    t.left(1)
t.forward(1)
t.end_fill()
t.left(90)
print(t.heading())
#body
t.speed(0)
t.color("brown")
t.penup()
t.goto(-130,80)
t.right(90)
t.pendown()
t.begin_fill()
t.forward(130)
for i in range(180):
    t.forward(2)
    t.left(1)
t.forward(130)
for i in range(45):
    t.forward(8)
    t.left(4)
t.end_fill()
t.left(180)
