import turtle
safhe = turtle.Screen()
safhe.setup(1280 , 720)
safhe.title("a moving car")
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t.hideturtle()
t2.hideturtle()
t3.hideturtle()


safhe.bgcolor("#22092C")
t.pencolor("white")
sorat = turtle.textinput("sorat","sorat mashin ra vared konid")
sorat = int(sorat)
#t2:
t2._delay(0)

t2.penup()
t2.pencolor("white")
t2.goto (-2*1280/2, -40)
t2.left(90)
t2.backward(50)
t2.right(90)
t2.pendown()
t2.forward(5000)

#t1 :
t._delay(0)
t.speed(100)
a = 1
t.penup()



while a < 2000:
    t.fillcolor("black")
    t.begin_fill()
    t.forward(70)
    t.right(45)
    t.forward(50)
    t.left(45)
    #kapot
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(25) #50
    #charkh e 1
    t.right(90)
    t.circle(15)
    t.left(90)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(100)
    t.right(90)
    #charkh e 2
    t.circle(15)
    t.left(90)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(25)
    t.right(90)
    t.forward(40)
    t.right(45)
    t.forward(50)
    t.right(45)
    t.forward(30)
    #shishe1 :
    t.penup()
    t.backward(15) #fasele ofoghi
    t.right(135)
    t.forward(10) #fasele amoodi
    t.pendown()
    t.forward(40)
    t.left(135)
    t.forward(60)
    t.left(90)
    t.forward(28)
    t.left(90)
    t.forward(33)
    t.penup()
    t.backward(45) #fasele bein e do shishe
    t.pendown()
    #shishe2 :
    t.left(90)
    t.forward(28)
    t.left(90)
    t.forward(60)
    t.left(135)
    t.forward(40)
    t.left(45)
    t.forward(33)
    t.end_fill()
    t.clear()
    a = a + 1
    t.penup()
    b = a * sorat
    t.goto(1280/2*-1+b , 0)
    t.pendown()
    t.right(180)

