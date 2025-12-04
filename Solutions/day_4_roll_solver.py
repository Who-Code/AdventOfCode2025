
import os


def parse_rolls(path):
    with open(os.path.join(os.path.dirname(__file__), path), "r", encoding="utf-8") as handle:
        return [line.rstrip("\n") for line in handle if line.strip()]


def count_accessible_rolls(grid_lines):
    grid = [list(line) for line in grid_lines]
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    accessible = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            nearby = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    nearby += 1
            if nearby < 4:
                accessible += 1

    return accessible


def main():
    print("looks a bit like a toilet ===>>>>")
    grid_lines = parse_rolls("day_4_roll_input.txt")
    print(count_accessible_rolls(grid_lines))


if __name__ == "__main__":
    main()
