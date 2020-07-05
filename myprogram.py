
import sys

def magix(line):
    print (line)

def magix_this_file_name(file_name):
    try:
        this_file = open(file_name, "r")
        lines = this_file.readlines()
        for line in lines:
            magix(line)
    except IOError as e:
        return e

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_names = sys.argv[1:]
        for file_name in file_names:
            magix_this_file_name(file_name)
    else:
        for line in sys.stdin:
            magix(line)
