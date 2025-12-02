import os

def parse_ids(path):
    with open(os.path.join(os.path.dirname(__file__), path), "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            ids = stripped.split(",")
            return ids

def is_valid(id):


def main():
    print("Happy second day =>>>")
    ids = list(parse_ids("day_2_ids_input.txt"))
    print(ids)

if __name__ == "__main__":
    main()
