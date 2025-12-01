import os

def parse_rotations(path):
    with open(os.path.join(os.path.dirname(__file__), path), "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                yield stripped[0], int(stripped[1:])

def track_dial(rotations):
    numbers = list(range(100))
    index = numbers.index(50)
    hits = 0
    for direction, distance in rotations:
        if direction == "L":
            index = (index - distance) % len(numbers)
        elif direction == "R":
            index = (index + distance) % len(numbers)
        if numbers[index] == 0:
            hits += 1
    return hits

def track_dial_part2(rotations):
    numbers = list(range(100))
    index = numbers.index(50)
    hits = 0
    for direction, distance in rotations:
        if direction == "L":
            step = -1
        elif direction == "R":
            step = 1
        else:
            continue
        for _ in range(distance):
            index = (index + step) % len(numbers)
            if numbers[index] == 0:
                hits += 1
    return hits

def main():
    print("Merry Christmas and lets go xD =>>>")
    rotations = list(parse_rotations("day_1_dial_input.txt"))
    print(track_dial(rotations))
    print(track_dial_part2(rotations))

if __name__ == "__main__":
    main()
