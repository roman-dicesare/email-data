import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py <file_path>")
        sys.exit(1)
    else:
        user_input = sys.argv[1]
        print(user_input)
        sys.exit(0)


main()