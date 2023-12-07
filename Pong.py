def pong():
    import turtle
    import sys
    import time
    # import winsound

    wn=turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    score_a=0
    score_b=0

    paddle_a=turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350,0)


    paddle_b=turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350,0)

    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.shapesize()
    ball.penup()
    ball.goto(0,0)
    ball.dx=0.5
    ball.dy=0.5

    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)


    def paddle_a_up():
        y=paddle_a.ycor()
        y+=20
        paddle_a.sety(y)

    def paddle_a_down():
        y=paddle_a.ycor()
        y-=20
        paddle_a.sety(y)

    def paddle_b_up():
        y=paddle_b.ycor()
        y+=20
        paddle_b.sety(y)

    def paddle_b_down():
        y=paddle_b.ycor()
        y-=20
        paddle_b.sety(y)

    wn.listen()
    wn.onkey(paddle_a_up, "w")
    wn.onkey(paddle_a_down, "s")
    wn.onkey(paddle_b_up, "Up")
    wn.onkey(paddle_b_down, "Down")



    while True:
        wn.update()
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        if ball.ycor()>290:
            ball.sety(290)
            ball.dy*=-1.0025

        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy*=-1.0025
        
        if ball.xcor()> 390:
            ball.goto(0,0)
            ball.dx *= -1.0025
            score_a+=1
            # winsound.PlaySound("rubber-ball-bouncing-98700.WAV",winsound.SND_ASYNC)
        
        if ball.xcor()< -390:
            ball.goto(0,0)
            ball.dx *= -1.0025
            score_b+=1
            # winsound.PlaySound("rubber-ball-bouncing-98700.WAV",winsound.SND_ASYNC)

        if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor () < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40) :
            ball.setx(340)
            ball.dx *= -1.0025

        if ball.xcor() < -340 and ball.xcor()> -350 and (ball.ycor () < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40) :
            ball.setx(-340)
            ball.dx *= -1.0025
        pen.clear()
        pen.write(f"Player A: {score_a} | | Player B:{score_b}" , align="center" , font=("courier", 24 , "normal"))

        if score_a>=3:
            ball.goto(0,0)
            paddle_a.goto(-350,0)
            paddle_b.goto(350,0)
            ball.dx *= 0
            pen.clear()
            pen.write("Game over! Player A wins" , align="center" , font=("courier", 24 , "normal"))
            user_input = turtle.textinput("INPUT", "Wanna play again \n Y if yes \n N for no \n\n :").lower()
            if user_input=="y":
                wn.clear()
                pong()
            elif user_input=='n':
                pen.clear()
                pen.write("THANK YOU FOR PLAYING!" , align="center" , font=("courier", 24 , "normal"))
                time.sleep(3)
                sys.exit()
                
                
        elif score_b>=3:
            ball.goto(0,0)
            ball.dx *= 0
            paddle_a.goto(-350,0)
            paddle_b.goto(350,0)
            pen.clear()
            user_input = turtle.textinput("INPUT", "Wanna play again \n Y if yes \n N for no \n\n :").lower()
            if user_input=="y":
                wn.clear()
                pong()
            elif user_input=='n':
                pen.clear()
                pen.write("THANK YOU FOR PLAYING!" , align="center" , font=("courier", 24 , "normal"))
                time.sleep(3)
                sys.exit()
pong()          





