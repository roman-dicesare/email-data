import sys, csv
from pprint import pprint
from data import normalize_DateSendStarted, read_email_data


def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py 'csv-files/<filename>")
        sys.exit(1)
    
    file_name: str = sys.argv[1]

    normalize_DateSendStarted(file_name)
    
    try:
        dataset = read_email_data(file_name)
    except FileNotFoundError:
        print("Error: That file doesn't exist. Try command again.")
        sys.exit(1)
    
    print(f"{file_name} is real and working.")
    print()

    for row in dataset[:1]:
        pprint(row, sort_dicts=False)
        print()

# we want to use CLI to tell it which file to open, and then what to do with that file.

    # open 'test.csv'
    # read something out of it
    # modulate that data it read
    # report back something (in this case test data)

    # want to be able to search by show (production)


main()