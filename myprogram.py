
import sys


def magix(file_name):
    try:
        this_file = open(file_name, "r")
        lines = this_file.readlines()
        return lines
    except IOError as e:
        return e


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_names = sys.argv[1:]
        for file_name in file_names:
            magix(file_name)
