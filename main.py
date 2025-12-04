import sys
# from pprint import pprint
from data import normalize_DateSendStarted, read_email_data

def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py 'csv-files/<filename>")
        sys.exit(1)
    
    file_name: str = sys.argv[1]
    
    try:
        dataset = read_email_data(file_name)
    except FileNotFoundError:
        print("Error: That file doesn't exist. Try command again.")
        sys.exit(1)

    
    first_row = dataset[0]
    raw_date = first_row["DateSendStarted"]
    normalized = normalize_DateSendStarted(raw_date)
    
    print(normalized)


main()