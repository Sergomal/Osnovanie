from tkinter import *
import random
import time
from tkinter import messagebox as mb


def move_ball(event):
    key = event.keysym.lower()
    x1, y1, x2, y2 = canvas.coords(ball)
    if key == "up" and y1 > 0:
        canvas.move(ball, 0, -20)
    elif key == "down" and y2 < 300:
        canvas.move(ball, 0, 20)
    elif key == "left" and x1 > 0:
        canvas.move(ball, -20, 0)
    elif key == "right" and x2 < 400:
        canvas.move(ball, 20, 0)
    check_collision()


def check_collision():
    ball_xy = canvas.coords(ball)
    square_xy = canvas.coords(square)
    if (
        ball_xy[2] > square_xy[0]
        and ball_xy[0] < square_xy[2]
        and ball_xy[3] > square_xy[1]
        and ball_xy[1] < square_xy[3]
    ):
        move_square()
        update_score()


def move_square():
    x1, y1 = random.randint(0, 380), random.randint(0, 280)
    x2, y2 = x1 + 20, y1 + 20
    canvas.coords(square, x1, y1, x2, y2)


def update_score():
    global score, start_time, pause
    score += 1
    score_label.config(text=f"Score: {score}")
    if score > 9:
        end_time = time.time()
        pause = True
        if end_time - start_time < 30:
            mb.showinfo(
                "Game Over",
                f"Game Over\nYour time is {(end_time - start_time):.1f}\nWIN!!!",
            )

        else:
            mb.showinfo(
                "Game Over",
                f"Game Over\nYour time is {(end_time - start_time):.1f}\nYou lost!!!",
            )
        if mb.askyesno("Game Over", "Do you want to play again?"):
            start_game()
            pause = False
            timer()
        else:
            window.quit()


def start_game():
    global score, start_time
    score = 0
    score_label.config(text=f"Score: {score}")
    start_time = time.time()
    time_label.config(text=f"Time: {(time.time() - start_time):.0f}")
    move_square()


def timer():
    global start_time, pause
    if not pause:
        time_label.config(text=f"Time: {(time.time() - start_time):.0f}")
    time_label.after(1000, timer)


window = Tk()
window.geometry("400x400")
window.title("Игра с шариком")

canvas = Canvas(window, width=400, height=300)
canvas.pack()

ball = canvas.create_oval(180, 180, 220, 220, fill="red", outline="black")
window.bind("<KeyPress>", move_ball)

square = canvas.create_rectangle(150, 150, 170, 170, fill="blue", outline="black")

score = 0
start_time = time.time()

score_label = Label(text=f"Score: {score}", font=("Arial", 16), fg="black", width=20)
score_label.pack(side=LEFT)

time_label = Label(
    text=f"Time: {time.time() - start_time:.0f}",
    font=("Arial", 16),
    fg="black",
    width=20,
)
time_label.pack(side=LEFT)


window.focus_set()
pause = False
start_game()
timer()

window.mainloop()
