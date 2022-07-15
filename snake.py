import turtle
import time
import random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
MARGIN=20 

def init_screen():
    pas=turtle.Screen()
    pas.title("snake game")
    pas.bgcolor("blue")
    pas.setup(height=SCREEN_WIDTH,width=SCREEN_HEIGHT)
    pas.tracer(0)
    return pas

def init_snake_head():
    head=turtle.Turtle()
    head.shape("square")
    head.color("black")
    head.speed(0)
    head.penup()
    head.goto(0,100)
    head.direction="stop"
    return head

def add_snake_length():
    t=turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("gray")
    t.penup()
    segments.append(t)
    return segments

def move(head):
    x,y=head.position()
    if head.direction=="up":
        head.sety(y+20)
    if head.direction=="down":
        head.sety(y-20)
    if head.direction=="right":
        head.setx(x+20)
    if head.direction=="left":
        head.setx(x-20)

def init_key_listener(b):
    b.listen()    
    b.onkey(go_up, "Up")
    b.onkey(go_down, "Down")
    b.onkey(go_right, "Right")
    b.onkey(go_left, "Left")

def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_right():
    if head.direction != "left":
        head.direction="right"
def go_left():
    if head.direction != "right":
        head.direction="left"

def init_food():
    f=turtle.Turtle()
    f.speed(0)
    f.shape('circle')
    f.color('red')
    f.penup()
    f.shapesize(0.5,0.5)
    f.goto(0,0)
    return f

def check_food(f,head):
    xf,yf = f.position()
    xh,yh = head.position()
    return abs(xh-xf) < 15 and abs(yf-yh) < 15

def reposition_food(f):
    half_width=SCREEN_WIDTH//2-MARGIN
    half_height=SCREEN_HEIGHT//2-MARGIN
    new_x=random.randint(-1* half_width, half_width)
    new_y=random.randint(-1* half_height, half_height)
    f.setpos(new_x,new_y)

def move_segments():
    if len(segments) > 0:
        for i in range(len(segments)-1, 0, -1):
            x_prev_seg, y_prev_seg = segments[i-1].position()
            segments[i].setpos(x_prev_seg, y_prev_seg)
        xh, yh = head.position()
        segments[0].setpos(xh, yh)   
        
def check_self_collision():
    for seg in segments:
        if seg.distance(head)<10:
            return True
    return False
    

def check_border_collision():
    half_width=SCREEN_WIDTH//2
    half_height=SCREEN_HEIGHT//2
    xh,yh = head.position()
    return xh>half_width or xh< -1*half_width or yh>half_height or yh<-1*half_height

def reset_game():
    for seg in segments:
        seg.goto(0,1000)
    segments.clear()
    food.goto(0,0)
    head.goto(0,100)
    head.direction="stop"

def init_score_writer():
    pen=turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    return pen

def update_score():
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.goto(0,260)
    score_writer.write("Score:{} High Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))


scrn=init_screen()
head=init_snake_head()
food=init_food()
score_writer=init_score_writer()
init_key_listener(scrn)
segments=[]
score=0
high_score=0

while True:  
    move_segments()
    move(head)
    if check_food(food, head):
        reposition_food(food)
        add_snake_length()   
        move(head)
        score = score + 10 

    if check_self_collision() or check_border_collision():
        if score>high_score:
            high_score=score
        score=0
        reset_game()

    update_score()
    scrn.update()
    time.sleep(0.2)
    
turtle.mainloop()

