#Juego de ping pong

import turtle


vn = turtle.Screen()
vn.title("Pong by ICI")
vn.bgcolor("black")
vn.setup(width=800, height=600)
vn.tracer(0)




#Score 
score_a = 0
score_b = 0

#Barra A
barra_a= turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()
barra_a.goto(-350, 0)



#Barra B 
barra_b= turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()
barra_b.goto(350, 0)


#Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = -.3


#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 PLayer B: 0",align= "center", font= ("Courier", 24, "normal"))



#function
def barra_a_up():
    y= barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barra_a_down():
    y= barra_a.ycor()
    y -= 20
    barra_a.sety(y)

def barra_b_up():
    y= barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barra_b_down():
    y= barra_b.ycor()
    y -= 20
    barra_b.sety(y)



#teclado juego  
vn.listen()
vn.onkeypress(barra_a_up, "w")
vn.onkeypress(barra_a_down, "s")
vn.onkeypress(barra_b_up, "Up")
vn.onkeypress(barra_b_down, "Down")

#main game loop 

while True:
    vn.update()
     

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #border checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} PLayer B: {}".format(score_a, score_b), align= "center", font= ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} PLayer B: {}".format(score_a, score_b), align= "center", font= ("Courier", 24, "normal"))


    # Barra y la colision

    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < barra_b.ycor() + 40 and ball.ycor() > barra_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
       
    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < barra_a.ycor() + 40 and ball.ycor() > barra_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1




    