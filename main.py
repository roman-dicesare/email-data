import sys
import csv


def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py 'csv-files/<filename>")
        sys.exit(1)
    
    file_name: str = sys.argv[1]
    
    try:
        opened_file = read_email_data(file_name)
    except FileNotFoundError:
        print("Error: That file doesn't exist. Try command again.")
        sys.exit(1)
    
    print(f"{file_name} is real and working.")

    print(opened_file)

# we want to use CLI to tell it which file to open, and then what to do with that file.

    # open 'test.csv'
    # read something out of it
    # modulate that data it read
    # report back something (in this case test data)

    # want to be able to search by show (production)

def read_email_data(file_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            rows.append(row)
        return rows


main()