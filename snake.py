"""
Snake Game in Python
Built with Python's standard library (turtle module). No installation needed!
"""

import turtle
import random

# -------------------------------------------------------------
# Configuration & Settings
# -------------------------------------------------------------
WIDTH = 800
HEIGHT = 600

# Speed settings (Delay in milliseconds between frames)
# Higher number = slower snake (easier); lower = faster
SPEED_EASY = 120    # 120ms
SPEED_MEDIUM = 90   # 90ms
SPEED_HARD = 60     # 60ms

DEFAULT_SPEED = SPEED_EASY
SPEED_INCREMENT = 1  # Speedup per food (ms)
MIN_SPEED = 40       # Fastest limit (ms)

# Theme Colors
COLOR_BG = "#1e1e2e"          # Dark slate background
COLOR_BORDER = "#45475a"      # Subtle border
COLOR_SNAKE_HEAD = "#506ffa"  # Vibrant green head
COLOR_SNAKE_BODY = "#2be468"  # Green body segments
COLOR_FOOD = "#883c3c"        # Bright red apple
COLOR_TEXT = "#f8f8f2"        # Off-white text

# -------------------------------------------------------------
# Game State
# -------------------------------------------------------------
score = 0
high_score = 0
delay = DEFAULT_SPEED
is_paused = False
game_over = False
segments = []

# -------------------------------------------------------------
# Screen Setup
# -------------------------------------------------------------
window = turtle.Screen()
window.title("Classic Snake Game")
window.bgcolor(COLOR_BG)
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)  # Smooth rendering

# Force window to the foreground and focus
try:
    root = window._root
    root.attributes("-topmost", True)
    root.update()
    root.attributes("-topmost", False)
    root.lift()
    root.focus_force()
except Exception:
    pass

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color(COLOR_BORDER)
border_pen.penup()
border_pen.setposition(-380, -280)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(2):
    border_pen.forward(760)
    border_pen.left(90)
    border_pen.forward(560)
    border_pen.left(90)
border_pen.hideturtle()

# -------------------------------------------------------------
# Snake Head
# -------------------------------------------------------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(COLOR_SNAKE_HEAD)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# -------------------------------------------------------------
# Food
# -------------------------------------------------------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(COLOR_FOOD)
food.penup()
food.goto(0, 100)

# -------------------------------------------------------------
# Scoreboard & Message Pens
# -------------------------------------------------------------
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color(COLOR_TEXT)
hud.penup()
hud.hideturtle()
hud.goto(0, 255)

message_pen = turtle.Turtle()
message_pen.speed(0)
message_pen.color(COLOR_TEXT)
message_pen.penup()
message_pen.hideturtle()
message_pen.goto(0, 0)


def show_start_prompt():
    """Displays controls to start playing."""
    message_pen.clear()
    message_pen.goto(0, 40)
    message_pen.color("#8be9fd")
    message_pen.write("Press Arrow Keys or WASD to Start", align="center", font=("Courier", 14, "bold"))
    message_pen.goto(0, 10)
    message_pen.color(COLOR_TEXT)
    message_pen.write("SPACE: Pause  |  R: Restart", align="center", font=("Courier", 11, "normal"))


def update_score_display():
    """Updates the score text at the top."""
    hud.clear()
    hud.write(
        f"Score: {score}   |   High Score: {high_score}",
        align="center",
        font=("Courier", 16, "bold"),
    )


def show_game_over():
    """Displays Game Over text."""
    message_pen.clear()
    message_pen.goto(0, 30)
    message_pen.color("#ff5555")
    message_pen.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
    message_pen.goto(0, -15)
    message_pen.color(COLOR_TEXT)
    message_pen.write("Press 'R' or 'Space' to Play Again", align="center", font=("Courier", 14, "normal"))


def show_pause(paused):
    """Displays Pause overlay."""
    message_pen.clear()
    if paused:
        message_pen.goto(0, 0)
        message_pen.color("#f1fa8c")
        message_pen.write("PAUSED (Press SPACE to Resume)", align="center", font=("Courier", 16, "bold"))


def spawn_food():
    """Places food at a random grid cell not overlapping the snake."""
    while True:
        x = random.randint(-18, 18) * 20
        y = random.randint(-13, 13) * 20
        if head.distance(x, y) < 15:
            continue
        if any(segment.distance(x, y) < 15 for segment in segments):
            continue
        food.goto(x, y)
        break


# -------------------------------------------------------------
# Movement & Controls
# -------------------------------------------------------------
def go_up():
    if head.direction != "down" and not is_paused and not game_over:
        if head.direction == "stop":
            message_pen.clear()
        head.direction = "up"


def go_down():
    if head.direction != "up" and not is_paused and not game_over:
        if head.direction == "stop":
            message_pen.clear()
        head.direction = "down"


def go_left():
    if head.direction != "right" and not is_paused and not game_over:
        if head.direction == "stop":
            message_pen.clear()
        head.direction = "left"


def go_right():
    if head.direction != "left" and not is_paused and not game_over:
        if head.direction == "stop":
            message_pen.clear()
        head.direction = "right"


def toggle_pause():
    global is_paused
    if game_over:
        reset_game()
        return
    is_paused = not is_paused
    show_pause(is_paused)


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


# -------------------------------------------------------------
# Game Reset
# -------------------------------------------------------------
def reset_game():
    """Resets snake and game state."""
    global score, delay, game_over, is_paused, segments

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    head.goto(0, 0)
    head.direction = "stop"

    spawn_food()

    score = 0
    delay = DEFAULT_SPEED
    game_over = False
    is_paused = False

    update_score_display()
    show_start_prompt()


# -------------------------------------------------------------
# Key Bindings
# -------------------------------------------------------------
window.listen()

# Arrow keys
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# WASD keys
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(go_up, "W")
window.onkeypress(go_down, "S")
window.onkeypress(go_left, "A")
window.onkeypress(go_right, "D")

# Restart & Pause
window.onkeypress(reset_game, "r")
window.onkeypress(reset_game, "R")
window.onkeypress(toggle_pause, "space")


# -------------------------------------------------------------
# Main Game Loop (Driven by turtle.ontimer)
# -------------------------------------------------------------
def game_loop():
    global score, high_score, delay, game_over

    try:
        if not is_paused and not game_over and head.direction != "stop":
            # Check border collision (-380 to +380 X, -280 to +280 Y boundary)
            if (
                head.xcor() > 365
                or head.xcor() < -365
                or head.ycor() > 265
                or head.ycor() < -265
            ):
                game_over = True
                show_game_over()

            # Check collision with food
            elif head.distance(food) < 20:
                spawn_food()

                # Add a new segment to snake body
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color(COLOR_SNAKE_BODY)
                new_segment.penup()
                segments.append(new_segment)

                # Update score
                score += 10
                if score > high_score:
                    high_score = score
                update_score_display()

                # Gradually speed up
                if delay > MIN_SPEED:
                    delay = max(MIN_SPEED, delay - SPEED_INCREMENT)

            # Move segments in reverse order
            if not game_over:
                for index in range(len(segments) - 1, 0, -1):
                    x = segments[index - 1].xcor()
                    y = segments[index - 1].ycor()
                    segments[index].goto(x, y)

                if len(segments) > 0:
                    segments[0].goto(head.xcor(), head.ycor())

                # Move head forward
                move()

                # Check self-collision
                for segment in segments:
                    if segment.distance(head) < 15 and head.direction != "stop":
                        game_over = True
                        show_game_over()
                        break

        window.update()
        # Schedule the next frame
        window.ontimer(game_loop, delay)

    except (turtle.Terminator, Exception):
        # Window closed by user
        pass


def run_game():
    update_score_display()
    show_start_prompt()
    window.update()
    window.ontimer(game_loop, delay)
    try:
        window.mainloop()
    except (turtle.Terminator, Exception):
        pass


if __name__ == "__main__":
    run_game()
