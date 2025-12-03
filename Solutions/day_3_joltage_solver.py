import os

def parse_joltages(path):
    joltage_lines = []
    with open(os.path.join(os.path.dirname(__file__), path), "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            joltage_lines.append(stripped)
    return joltage_lines
def highest_joltage(joltage_line):
    current_highest = 0
    joltage_list = list(joltage_line)
    # loop trough the joltage items
    for idx, joltage in enumerate(joltage_list):
        sub_joltage_list = joltage_list[idx+1:len(joltage_list)]
        for joltage_second in sub_joltage_list:
            current_value = int(joltage+joltage_second);
            if current_value > current_highest:
                current_highest = current_value
    return current_highest


def joltage_sum(joltage_lines):
    sum = 0
    for line in joltage_lines:
        sum += highest_joltage(line)
    return sum

def main():
    print("lets solve the joltage and start the elevators =>>>")
    joltage_lines = parse_joltages("day_3_joltage_input.txt")
    print(joltage_sum(joltage_lines))

if __name__ == "__main__":
    main()