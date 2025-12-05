
import os


def parse_rolls(path):
    with open(os.path.join(os.path.dirname(__file__), path), "r", encoding="utf-8") as handle:
        return [line.rstrip("\n") for line in handle if line.strip()]


def count_accessible_rolls(grid_lines):
    grid = _build_grid(grid_lines)
    return sum(1 for _ in _accessible_positions(grid))


def count_total_removed_rolls(grid_lines):
    grid = _build_grid(grid_lines)
    removed = 0

    while True:
        accessible = list(_accessible_positions(grid))
        if not accessible:
            break
        removed += len(accessible)
        for r, c in accessible:
            grid[r][c] = "."

    return removed


DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def _build_grid(grid_lines):
    return [list(line) for line in grid_lines]


def _accessible_positions(grid):
    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            nearby = 0
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    nearby += 1
            if nearby < 4:
                yield (r, c)


def main():
    print("looks a bit like a toilet ===>>>>")
    grid_lines = parse_rolls("day_4_roll_input.txt")
    print(count_accessible_rolls(grid_lines))
    print(count_total_removed_rolls(grid_lines))


if __name__ == "__main__":
    main()
