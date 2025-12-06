import sys
# from pprint import pprint
import data

def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py 'csv-files/<filename>")
        sys.exit(1)
    
    file_name: str = sys.argv[1]
    
    try:
        dataset = data.read_email_data(file_name)
    except FileNotFoundError:
        print("Error: That file doesn't exist. Try command again.")
        sys.exit(1)

    print(data.get_datetime(dataset, 6)) #how can we eliminate magic numbers here?  

main()