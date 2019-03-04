from tkinter import *
import random
import time

WIDTH = 1000
HEIGHT = 500
counter = 0
counter1 = 0
tk = Tk()
tk.title("Project Pong Game")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black", bd=0, highlightthickness=0)
tk.resizable(0, 0)
canvas.pack()
canvas.create_line(500, 0, 500, 500, fill="cyan")
score = canvas.create_text(230, 40, text=counter, font=("Arial", 60), fill="cyan")
score1 = canvas.create_text(730, 40, text=counter1, font=("Arial", 60), fill="cyan")


class Ball:
    def __init__(self, canvas, paddle, paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.ball = self.canvas.create_oval(10, 10, 30, 30, fill="yellow")
        self.canvas.move(self.ball, 480, 230)
        starts = [-3, 3]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]

    # LOGIC FOR Ball Hitting the Paddle
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.block)
        if paddle_pos[1] <= pos[1] <= paddle_pos[3]:  # pos[2]=right pos[0]=left
            if paddle_pos[0] <= pos[0] <= paddle_pos[2]:  # pos[3]=bottom pos[1]=top
                return True
            return False

    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.block)
        if paddle_pos[1] <= pos[1] <= paddle_pos[3]:  # pos[2]=right pos[0]=left
            if paddle_pos[0] <= pos[2] <= paddle_pos[2]:  # pos[3]=bottom pos[1]=top
                return True
            return False

    def draw(self):
        self.canvas.move(self.ball, self.x, self.y)
        pos = canvas.coords(self.ball)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= HEIGHT:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(False)
        if pos[2] >= WIDTH:
            self.x = -3
            self.score(True)
        if self.hit_paddle(pos):
            self.x = 3
        if self.hit_paddle1(pos):
            self.x = -3

    def score(self, val):
        global counter
        global counter1
        global score
        global score1
        if val:
            canvas.itemconfig(score, fill="black")
            counter += 1
            score = self.canvas.create_text(230, 40, text=counter, font=("Arial", 60), fill="cyan")
        else:
            self.canvas.itemconfig(score1, fill="black")
            counter1 += 1
            score1 = self.canvas.create_text(730, 40, text=counter1, font=("Arial", 60), fill="cyan")


class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.block = self.canvas.create_rectangle(0, 150, 30, 250, fill="red")
        self.y = 0
        self.canvas.bind_all('s', self.turn_down)
        self.canvas.bind_all('w', self.turn_up)

    def turn_down(self, event):
        self.y = 2

    def turn_up(self, event):
        self.y = -2

    def draw(self):
        self.canvas.move(self.block, 0, self.y)
        pos = self.canvas.coords(self.block)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= HEIGHT:
            self.y = 0


class Paddle1:
    def __init__(self, canvas):
        self.canvas = canvas
        self.block = self.canvas.create_rectangle(970, 150, 1000, 250, fill="blue")
        self.y = 0
        self.canvas.bind_all('<Down>', self.turn_down)
        self.canvas.bind_all('<Up>', self.turn_up)

    def turn_down(self, event):
        self.y = 2

    def turn_up(self, event):
        self.y = -2

    def draw(self):
        self.canvas.move(self.block, 0, self.y)
        pos = self.canvas.coords(self.block)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= HEIGHT:
            self.y = 0


paddle = Paddle(canvas)
paddle1 = Paddle1(canvas)
ball = Ball(canvas, paddle, paddle1)

while True:
    paddle.draw()
    paddle1.draw()
    ball.draw()
    tk.update()
    time.sleep(0.01)
    if counter >= 5:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(500, 220, text="PLAYER 1 WINS!!!", font=("Arial", 60), fill="cyan")
        canvas.itemconfig(score, fill="black")
        canvas.itemconfig(score1, fill="black")
        tk.update()
        time.sleep(10)

    if counter1 >= 5:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(500, 220, text="PLAYER 2 WINS!!!", font=("Arial", 60), fill="cyan")
        canvas.itemconfig(score, fill="black")
        canvas.itemconfig(score1, fill="black")
        tk.update()
        time.sleep(10)

tk.mainloop()