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

def main():
    print("Happy second day =>>>")
    ids = list(parse_ids("day_2_ids_input.txt"))
    invalid_ids = get_invalid_ids(ids)
    print(invalid_ids)
    print(sum(invalid_ids))

if __name__ == "__main__":
    main()
