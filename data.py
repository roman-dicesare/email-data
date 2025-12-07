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
        dt = datetime.strptime(cleaned_data,"%m/%d/%Y %I:%M:%S %p")
    except ValueError:
        print("Error when attempting to convert datetime")
        sys.exit(1)
    
    return dt

def get_datetime(dataset, row_number):
    data_row = dataset[row_number]
    raw_date = data_row["DateSendStarted"]
    normalized_date : str = normalize_DateSendStarted(raw_date)
    return normalized_date

def get_campaign(dataset, row_number):
    data_row = dataset[row_number]
    campaign_name = data_row["Campaign"]
    return campaign_name

def get_totalOpens(dataset, row_number):
    data_row = dataset[row_number]
    totalOpens = data_row["TotalOpens"]
    return totalOpens

def get_engagementRate(dataset, row_number):
    data_row = dataset[row_number]
    engagementRate : float = data_row["EngagementRate"]
    return engagementRate

def get_total_rows_in_data(dataset):
    total_data_rows = 0 #this assumes the first row is headers
    for row in dataset:
        total_data_rows += 1
    return total_data_rows

def get_best_performer(dataset):
    total_rows_in_set = get_total_rows_in_data(dataset)
    best_performer = dataset[1]["EngagementRate"]
    best_performer_campaign = ""

    for i in range(1, total_rows_in_set):
        data_row = dataset[i]
        data_in_row_engagement = data_row["EngagementRate"]
        data_in_row_campaign = data_row["Campaign"]
        if data_in_row_engagement > best_performer:
            best_performer = data_in_row_engagement
            best_performer_campaign = data_in_row_campaign
    return best_performer, best_performer_campaign