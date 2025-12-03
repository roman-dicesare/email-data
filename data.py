from datetime import datetime
import sys, csv

def read_email_data(file_name):
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            rows.append(row)
        return rows
    

def normalize_DateSendStarted(raw_data):
    if raw_data is None:
        sys.exit(1)
    
    cleaned_data = raw_data.strip() # this removes whitespace

    try:
        dt = datetime.strptime(cleaned_data, "%m/%d/%Y %H:%M")
    except ValueError:
        print("Error when attempting to convert datetime")
        sys.exit(1)
    
    return dt