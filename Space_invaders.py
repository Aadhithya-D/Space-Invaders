# making space invaders game
import turtle
import winsound
import math
import random

try:

    # set up screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Aadhi's Space Invaders")
    screen.bgpic("background.gif")
    turtle.register_shape("invader.gif")
    turtle.register_shape("player.gif")

    # making border
    border = turtle.Turtle()
    border.speed(0)
    border.color("white")
    border.penup()
    border.setposition(-300, -300)
    border.pendown()
    border.pensize(2)
    for side in range(4):
        border.fd(600)
        border.lt(90)
    border.hideturtle()

    score = 0
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("white")
    score_pen.penup()
    score_pen.setposition(-290, 280)
    scoreString = "Score: %s" % score
    score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    # making player
    import turtle

    player = turtle.Turtle()
    player.color("blue")
    player.shape("player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)

    playerspeed = 20

    number_of_enemies = 5
    enemies = []

    for i in range(number_of_enemies):
        # creating enemy
        enemies.append(turtle.Turtle())
    for enemy in enemies:
        enemy.color("red")
        enemy.shape("invader.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

    enemyspeed = 5

    # creating player's bullet
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    bulletspeed = 30
    bulletState = "ready"

    # moving player left and right and bullet


    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = -280
        player.setx(x)


    def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)


    def fire_bullet():
        # declare bulletstate as golbal if it needs to be changed
        global bulletState
        if bulletState == "ready":
            winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            bulletState = "fire"
            # move bulet above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()


    def iscollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if distance < 20:
            return True
        else:
            return False


    # making keyboard bindings
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    turtle.onkey(fire_bullet, "space")

    # main game loop
    while True:

        # making bullet move
        if bulletState == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        # making bullet not move when it reaches the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletState = "ready"

        for enemy in enemies:

            # moving enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            # move the enemy inside the border
            if enemy.xcor() > 280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            if enemy.xcor() < -280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            # collision
            if iscollision(bullet, enemy):
                winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
                bullet.hideturtle()
                bulletState = "ready"
                bullet.setposition(0, -400)
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setposition(x, y)
                score += 10
                scoreString = "Score: %s" % score
                score_pen.clear()
                score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

            if iscollision(player, enemy):
                winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
                player.hideturtle
                enemy.hideturtle
                print("Game over")
                exit()
            if enemy.ycor() < -280:
                print("Game over")
                exit()
    delay = input("press enter to finish.")


except:
    print("Game over")
