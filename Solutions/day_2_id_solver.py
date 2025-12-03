import os

def parse_ids(path):
    with open(os.path.join(os.path.dirname(__file__), path), "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            ids = stripped.split(",")
            return ids

def is_valid(id):
    id_str = str(id)
    length = len(id_str)
    if length % 2 != 0:
        return False
    half = length // 2
    return id_str[:half] == id_str[half:]

def get_invalid_ids(ids):
    invalid_ids = []
    for id in ids:
        if not id:
            continue
        start_str, end_str = id.split("-")
        start = int(start_str)
        end = int(end_str)
        for value in range(start, end + 1):
            if is_valid(str(value)):
                invalid_ids.append(value)
    return invalid_ids

def has_repeated_pattern(id):
    id_str = str(id)
    length = len(id_str)
    for size in range(1, length // 2 + 1):
        if length % size != 0:
            continue
        repeat_count = length // size
        if repeat_count < 2:
            continue
        segment = id_str[:size]
        if segment * repeat_count == id_str:
            return True
    return False

def get_invalid_ids_with_repeats(ids):
    invalid_ids = []
    for id in ids:
        if not id:
            continue
        start_str, end_str = id.split("-")
        start = int(start_str)
        end = int(end_str)
        for value in range(start, end + 1):
            if has_repeated_pattern(str(value)):
                invalid_ids.append(value)
    return invalid_ids

def main():
    print("Happy second day =>>>")
    ids = list(parse_ids("day_2_ids_input.txt"))
    invalid_ids = get_invalid_ids(ids)
    #print(invalid_ids)
    print(sum(invalid_ids))
    invalid_ids_repeats = get_invalid_ids_with_repeats(ids)
    #print(invalid_ids_repeats)
    print(sum(invalid_ids_repeats))

if __name__ == "__main__":
    main()
