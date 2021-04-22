import time
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=510, height=458)
wn.bgpic("sensor-bg-2.gif")
wn.title("Elsa Wind Sensor")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(8)

def draw_arrow(val, pen):
    # Draw hand
    pen.penup()
    pen.goto(1, -13)
    pen.color("gold")
    pen.setheading(90)
    angle = (val / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

def draw_text(text, pen):
    # Draw hand
    pen.penup()
    pen.goto(0, -120)
    pen.color("black")
    pen.write(text, move=False, align="center", font=("Helvetica", 24, "bold"))
    
while True:
    val = int(time.strftime("%s"))
    draw_text(val, pen)
    draw_arrow(val, pen)
    wn.update()
    time.sleep(1)
    pen.clear()
    
wn.mainloop()


