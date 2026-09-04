# AGENTS.md - Project Rules & Conventions

## 📌 Project Overview
This project is a lightweight, classic 2D Snake game implemented in Python. It is designed to be accessible, beginner-friendly, and completely self-contained with **zero external dependencies**.

---

## 🛠️ Architecture & Technology Stack

- **Language:** Python 3.x
- **Graphics & UI:** Python standard library `turtle` module (Tkinter wrapper).
- **Execution Model:**
  - Uses `window.ontimer()` coupled with `window.mainloop()` for frame scheduling.
  - **Do NOT** use blocking `while True: time.sleep()` loops, as they block the Windows message queue and cause window freeze / "Not Responding" states.
- **Coordinate & Grid System:**
  - Screen dimensions: 800x600 px.
  - Inner playfield: Boundaries at `[-380, 380]` in X and `[-280, 280]` in Y direction.
  - Grid step: `20px` increments for movement, body segments, and food placement.
  - Valid spawn coordinate range: X `[-360, 360]`, Y `[-260, 260]` (steps of 20).

---

## 📋 Core Development Rules & Guidelines

1. **Zero External Dependencies:**
   - Always prioritize Python's standard library (`turtle`, `time`, `random`, `math`, `tkinter`).
   - Do not introduce external packages (such as `pygame` or `pillow`) unless explicitly requested by the user.

2. **Clean Window Lifecycle & Safe Termination:**
   - Handle window closing gracefully by wrapping event loops in `except (turtle.Terminator, Exception): pass`.
   - Ensure closing the game window via the `X` button never produces unhandled terminal tracebacks.

3. **Window Focus Management:**
   - Keep window bring-to-front logic on initialization (`root.attributes("-topmost", True)` toggled back to `False` followed by `root.lift()` and `root.focus_force()`) so the game window receives focus when launched on Windows.

4. **Dual Controls:**
   - Maintain support for both **Arrow keys** (`Up`, `Down`, `Left`, `Right`) and **WASD** (`w`, `a`, `s`, `d`, case-insensitive).
   - Reserve `Spacebar` for Pause / Resume and `R` for Reset / Restart.

---

## 🎨 Styling & Theming Conventions

- **Color Scheme:** Dark modern palette (Hex codes):
  - Background: `#1e1e2e` (Dark slate)
  - Border: `#45475a` (Muted gray)
  - Snake Head: `#50fa7b` (Vibrant neon green)
  - Snake Body: `#2be468` (Bright green)
  - Food: `#ff5555` (Red apple)
  - UI Text: `#f8f8f2` (Off-white)
- **Typography:** Monospaced font (`Courier`) for retro arcade alignment and clean score display.

---

## 🚀 Running & Verification

- **Syntax Validation:**
  ```bash
  python -m py_compile snake.py
  ```
- **Local Execution:**
  - Launch via `python snake.py` or double-click `play.bat` on Windows.
  - *Note for AI Agents:* Agent subshell executions run in background sessions that cannot render GUI windows directly to the user's interactive desktop. Always instruct the user to run the script or batch file in their own terminal or via File Explorer.
