
# Advent of Code 2024

This project contains the solutions for the Advent of Code 2024 using Python 3.10.15.

## Requirements
- Python 3.10.15
- Make (optional)

## Configuration
1. Create the virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project structure
```
AdventOfCode/
├── day01/
│   ├── input.txt
│   └── first.py
│   └── second.py
├── shared/
│   └── utils.py
├── venv/
├── Makefile
└── README.md
```

## Usage
### Makefile Targets.

- **Create a new day (`create_day`)**
Creates a new folder for a specific day with a `first.py` file, another `second.py` and `input.txt`. In addition, it creates a new branch in the repository associated with the day and makes an initial commit.
```bash
make create_day DAY=01
```

- **Execute a specific day (`run`)**
Runs the solution script for the specified day.
```bash
make run DAY=01
```

- **Integrate changes to the `main` branch (`merge_to_main`)**
Integrates changes from the current day's branch (`dayXX`) into the `main` branch. It also deletes the `main` branch both locally and remotely.
```bash
make merge_to_main DAY=01
```

## Branching strategy

1. Starting a new day

Create a new branch for the specific day from the main branch:

```bash
git checkout dev
git pull origin dev
git checkout -b dayXX
```

2. Development
Work on the branch of the day (dayXX), making sure to keep the changes specific to that day. Add files and perform commits regularly:

```bash
git add .
git commit -m "Add solution for day XX"
```

3. Integration to main

Once the solution is finished and tested, merge dayXX to main:

```bash
git checkout main
git merge dayXX
```

### Flow

```
main
  |
  |--- day01
  |--- day02
  |--- day03
```