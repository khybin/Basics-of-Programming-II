
import turtle

screen = turtle.Screen()
screen.title("부드러운 Turtle 이동")
screen.setup(800, 600)
screen.bgcolor("white")
screen.tracer(0)  # 자동 화면 갱신 끄기

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.pensize(3)

# 이동 설정
move_speed = 4

# 방향키 상태 저장
keys = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

# 키를 누르면 True
def key_down(key):
    keys[key] = True

# 키를 떼면 False
def key_up(key):
    keys[key] = False

# 계속 움직이는 함수
def move():
    if keys["Up"]:
        t.setheading(90)
        t.forward(move_speed)

    if keys["Down"]:
        t.setheading(270)
        t.forward(move_speed)

    if keys["Left"]:
        t.setheading(180)
        t.forward(move_speed)

    if keys["Right"]:
        t.setheading(0)
        t.forward(move_speed)

    screen.update()
    screen.ontimer(move, 16)  # 약 60FPS

# 키 입력 연결
for key in keys:
    screen.onkeypress(lambda k=key: key_down(k), key)
    screen.onkeyrelease(lambda k=key: key_up(k), key)

screen.listen()
move()

screen.mainloop()
