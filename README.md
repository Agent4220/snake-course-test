# 🐍 Classic Snake Game in Python

A lightweight, beginner-friendly Snake game built entirely with Python's standard library (`turtle`). 

**No external libraries or `pip install` required!** It runs directly on Windows, macOS, and Linux right out of the box.

---

## 🎮 Features

- **Zero Installation**: Uses Python's built-in `turtle` module.
- **Smooth Gameplay**: Modern dark theme with responsive controls.
- **Score & High Score**: Real-time score counter and high score tracker.
- **Dual Controls**: Supports both **Arrow keys** and **WASD** keys.
- **Pause & Restart**: Easily pause with `Space` and restart anytime with `R`.
- **Clean Code**: Well-commented, modular, and easy for beginners to understand and modify.

---

## 🚀 How to Run

### Step 1: Check Python
Make sure Python 3 is installed. Open PowerShell, Command Prompt, or your terminal and verify:
```bash
python --version
```

### Option A (Easiest — Double-Click):
Just double-click **`play.bat`** in this folder!

### Option B (From Terminal):
Open PowerShell, Command Prompt, or terminal in this folder and run:
```bash
python snake.py
```

---

## 🕹️ Controls

| Action | Primary Key | Alternate Key |
| :--- | :--- | :--- |
| **Move Up** | `↑` (Up Arrow) | `W` |
| **Move Down** | `↓` (Down Arrow) | `S` |
| **Move Left** | `←` (Left Arrow) | `A` |
| **Move Right** | `→` (Right Arrow) | `D` |
| **Pause / Resume** | `Spacebar` | — |
| **Restart Game** | `R` | — |
| **Exit** | Close the window | — |

---

## 📜 Rules of the Game

1. Press any direction key (`Arrow Keys` or `WASD`) to start moving.
2. Guide the green snake to collect the red food.
3. Each food eaten adds **+10 points** and grows the snake's length by one segment.
4. **Game Over** triggers if you hit the boundary walls or run into your own body.
5. Press **`R`** or **`Space`** to restart immediately.

---

## ⚙️ Customization (Make It Your Own)

Open [snake.py](snake.py) in any text editor or IDE to tweak game settings:

- **Change Difficulty / Speed:**
  Near line 16, you can change `DEFAULT_SPEED`:
  ```python
  DEFAULT_SPEED = SPEED_EASY    # 0.12s (Gentle & beginner-friendly)
  # DEFAULT_SPEED = SPEED_MEDIUM  # 0.09s (Standard pace)
  # DEFAULT_SPEED = SPEED_HARD    # 0.06s (Fast-paced challenge)
  ```

- **Change Colors:**
  Near line 25, customize the theme colors:
  ```python
  COLOR_BG = "#1e1e2e"          # Background color
  COLOR_SNAKE_HEAD = "#50fa7b"  # Snake head color
  COLOR_SNAKE_BODY = "#2be468"  # Snake body color
  COLOR_FOOD = "#ff5555"        # Apple / Food color
  ```

---

## 📂 Project Structure

```text
gemini course/
├── snake.py     # Main Python game script
└── README.md    # Instructions and guide
```
