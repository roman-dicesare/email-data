from datetime import datetime
import sys, csv

def print_data(dataset):
    for row in dataset:
        print(f"Campaign: {row["Campaign"]}")
        print(f"Engagement Rate: {row["EngagementRate"]}")
        print(f"Total Delivered : {row["TotalDelivered"]}")
        print()

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

def calculate_top_five(dataset, n):
    scored_rows = []

    for row in dataset:
        engagement_rate = row["EngagementRate"].strip(" %")
        row["EngagementRate"] = float(engagement_rate)
        scored_rows.append(row)

    sorted_rows = sorted(scored_rows, key = lambda row: row["EngagementRate"], reverse = True)

    top_five = sorted_rows[:n]

    return top_five

def filter_by_campaign(dataset, campaign_alias):
    upper_alias = campaign_alias.upper()

    matching_campaigns = []

    for row in dataset:
        campaign_name = row["Campaign"]
        if upper_alias in campaign_name.upper():
            matching_campaigns.append(row)
    
    return matching_campaigns

def calculcate_worst(dataset):

    worst = []

    worst_campaign = dataset[0]
    for row in dataset:
        if row["EngagementRate"] < worst_campaign["EngagementRate"]:
            worst_campaign = row
    worst.append(worst_campaign)
    return worst