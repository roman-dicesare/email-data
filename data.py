from datetime import datetime
import sys, csv, get_def

def read_email_data(file_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            rows.append(row)
        return rows
    #end

def normalize_DateSendStarted(raw_data):
    if raw_data is None:
        sys.exit(1)
    
    cleaned_data = raw_data.strip() # this removes whitespace

    try:
        dt = datetime.strptime(cleaned_data,"%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        print("Error when attempting to convert datetime")
        sys.exit(1)
    return dt
    #end

def handle_argvs():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py 'csv-files/<filename> [optional <campaign_initial>]")
        sys.exit(1)

    file_name: str = sys.argv[1]
    return file_name
    #end

def set_campaign_initial():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py 'csv-files/<filename> [optional <campaign_initial>]")
        sys.exit(1)

    return sys.argv[2]
    #end

def open_file(file_name):
    try:
        dataset = read_email_data(file_name)
    except FileNotFoundError:
        print("Error: That file doesn't exist. Try command again.")
        sys.exit(1)
    
    return dataset
    #end

def check_args(dataset):
    args = []

    for arg in sys.argv:
        args.append(arg)



    #end
    