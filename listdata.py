import sys
from loaddata import load_data

# listdata.py


def print_rows(data, limit):
    for i, row in enumerate(data):
        if i >= limit:
            break
        print(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python listdata.py <datafile> <limit>")
        sys.exit(1)

    datafile = sys.argv[1]
    limit = int(sys.argv[2])

    data = load_data(datafile)
    print_rows(data, limit)