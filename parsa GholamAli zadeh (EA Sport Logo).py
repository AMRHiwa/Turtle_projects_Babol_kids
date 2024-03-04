import turtle

kaghaz =turtle.Screen()
kaghaz.setup(600,600)
kaghaz.title("fc24")
kaghaz.bgcolor("black")

p = turtle.Turtle()
p.pencolor("white")

p.left(90)
p.penup()
p.forward(120)
p.left(90)
p.forward(95)
p.pendown()
#ea
p.fillcolor("white")
p.begin_fill()
p.left(180)
p.forward(200)
p.right(120)
p.forward(50)
p.right(60)
p.forward(170)
p.right(60)
p.forward(50)
p.end_fill()

p.pencolor("black")
p.penup()
p.right(120)
p.forward(110)
p.right(90)
p.forward(40)


p.write("EA SPORT", align='center', font= ("Arial", 20))
p.pencolor("white")



#مثلث

p.forward(15)
p.right(90)
p.forward(85)
p.pendown()

p.fillcolor("white")
p.begin_fill()

p.left(120)
p.forward(40)
p.left(120)
p.forward(40)
p.left(120)
p.forward(40)
p.end_fill()


#f

p.penup()
p.left(120)
p.forward(54)
p.pendown()

p.fillcolor("white")
p.begin_fill()

p.forward(26)
p.left(120)
p.forward(20)
p.right(60)
p.forward(45)
p.left(60)
p.forward(25)
p.left(120)
p.forward(40)
p.right(120)
p.forward(10)
p.right(60)
p.forward(40)
p.left(60)
p.forward(25)
p.left(120)
p.forward(60)
p.circle(20, 60)
p.forward(40)
p.end_fill()

p.penup()
p.left(60)
p.forward(115)
p.pendown()

#c
p.fillcolor("white")
p.begin_fill()

p.left(120)
p.forward(100)
p.left(120)
p.forward(15)
p.left(60)
p.forward(50)
p.right(110)
p.forward(5)
p.right(70)
p.forward(90)
p.right(70)
p.forward(5)
p.right(110)
p.forward(30)
p.left(120)
p.forward(15)
p.left(60)
p.forward(55)
p.left(120)
p.forward(27)
p.circle(20, 60)
p.forward(110)
p.circle(20, 60)
p.end_fill()


p.pencolor("black")
p.penup()
p.forward(110)
p.right(120)
p.forward(180)
p.pendown()

p.fillcolor("red")
p.begin_fill()
p.left(90)
p.forward(100)
p.left(90)
p.forward(300)
p.left(90)
p.forward(100)
p.left(90)
p.forward(300)
p.end_fill()


p.penup()
p.left(90)
p.forward(50)
p.left(90)
p.forward(150)



p.write("Emearates airwais", align='center', font= ("Arial", 24))
p.pencolor("white")

p.right(90)
p.forward(50)
p.write("FIFA.COM", align='center', font= ("Arial", 24))
p.pencolor("white")

p.forward(40)


p.write("PARSA.GH.G", align='center', font= ("Arial", 16))
p.pencolor("white")
p.forward(20)















