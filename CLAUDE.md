# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A classic 2D Snake game in a single file (`snake.py`), built only with the Python 3 standard library (`turtle`, `random`). No dependencies, no `pip install`, no build step. `README.md` is the player-facing guide.

## Commands

```bash
python -m py_compile snake.py   # syntax check — the only automated verification available
python snake.py                 # run the game (opens a Tkinter/turtle window)
```

`play.bat` is a Windows convenience wrapper (double-click) that `cd`s to the folder and runs `snake.py`.

There is no test suite, linter, or CI. There is no git repository.

**Agent limitation:** subshell runs cannot render a GUI to the user's desktop. Do not try to "run" the game to verify behavior — use `py_compile` and ask the user to launch it themselves.

## Architecture

Everything lives in `snake.py` as module-level code (no classes, no `main()` beyond `run_game()`). Structure top to bottom: config constants → mutable game-state globals → screen/border/head/food/HUD turtle objects → display functions → movement/control handlers → `reset_game()` → key bindings → `game_loop()` → `run_game()`.

Key design points a change must respect:

- **Frame scheduling is non-blocking.** `game_loop()` re-arms itself with `window.ontimer(game_loop, delay)` and the program is kept alive by `window.mainloop()`. Never introduce `while True` / `time.sleep()` loops — they freeze the Windows message queue ("Not Responding").
- **State is global.** Handlers and the loop mutate module globals (`score`, `high_score`, `delay`, `is_paused`, `game_over`, `segments`) via `global`. Keep this pattern rather than refactoring to a class unless asked.
- **`delay` is the difficulty knob.** Milliseconds between frames; starts at `DEFAULT_SPEED`, decremented by `SPEED_INCREMENT` per food down to `MIN_SPEED`. Lower = faster.
- **Grid.** 20px step for movement, body segments, and food. Playfield roughly ±380 X / ±280 Y; `game_loop()` uses ±365 / ±265 as the wall-collision test. Food spawns at `randint(-18,18)*20` / `randint(-13,13)*20`, re-rolled until clear of head and body.
- **Body follow.** Each frame, segments copy the position of the segment ahead (iterated in reverse), segment 0 takes the head's old position, then the head moves.
- **Clean shutdown.** Both `game_loop()` and `run_game()` wrap their bodies in `except (turtle.Terminator, Exception): pass` so closing the window never prints a traceback. Preserve this.
- **Windows focus hack.** The `root.attributes("-topmost", ...)` / `lift()` / `focus_force()` block near screen setup brings the window forward on launch — keep it.

## Conventions

- Standard library only. Do not add `pygame`, `pillow`, etc. unless the user explicitly asks.
- Dual controls: Arrow keys **and** WASD (both cases). `Space` = pause/resume (and restart when game over), `r`/`R` = restart.
- Dark theme via the `COLOR_*` constants; `Courier` monospaced font for all on-screen text.

## Note

`GEMINI.md` is an existing Gemini CLI ruleset covering the same conventions; `AGENTS.md` is empty. A Gemini config was detected — reply `/import` to see what can be imported into Claude Code, then `/import --yes=<digest>` to apply it.
