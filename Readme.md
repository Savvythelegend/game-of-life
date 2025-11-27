# Game of Life (Terminal Simulation)

A Python implementation of Conway’s Game of Life with a command-line interface.
Patterns are defined in a TOML file and rendered through a terminal view.

---

## Project Structure

```
savvythelegend-game-of-life/
├── Readme.md
├── pyproject.toml
└── src/
    └── rplife/
        ├── __init__.py
        ├── __main__.py
        ├── cli.py
        ├── grid.py
        ├── patterns.py
        ├── patterns.toml
        └── views.py
```

---

## Installation

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install the package:

```
pip install .
```

For development:

```
pip install -e .
```

---

## Command-Line Usage

Check available options:

```
rplife --help
```

Run with the default pattern and settings:

```
rplife
```

Run a specific pattern:

```
rplife --pattern Blinker
```

Run all patterns in sequence:

```
rplife --all
```

Set number of generations:

```
rplife --pattern Pulsar --gen 50
```

Set frames per second:

```
rplife --fps 12
```

Specify a view (if multiple views are available):

```
rplife --view CursesView
```

---

## Available Patterns

Patterns are defined in:

```
src/rplife/patterns.toml
```

Names in this file correspond to valid `--pattern` values.

---

## Running as a Module

```
python -m rplife
```

---

## Development Notes

* Package follows the `src/` layout.
* Version is defined in `rplife/__init__.py`.
* CLI entry point is configured in `pyproject.toml` under `[project.scripts]`.
