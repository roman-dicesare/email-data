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

def calculate_top_five(dataset, n):
    scored_rows = []

    for row in dataset:
        engagement_rate = (row["EngagementRate"]).strip(" %")
        scored_rows.append({"Campaign": row["Campaign"],
                            "Subject" : row["Subject"], 
                            "EngagementRate" : float(engagement_rate),
                            "TotalDelivered" : row["TotalDelivered"]})
    
    sorted_rows = sorted(scored_rows, key = lambda row: row["EngagementRate"], reverse = True)

    top_five = sorted_rows[:n]

    return top_five

def print_top_five_emails(dataset,n):
    top_five_rates = calculate_top_five(dataset, n)
    print(f"Top email campaigns:")
    print("-----")
    for item in top_five_rates:
        print(f"Campaign Name: {item['Campaign']}")
        print(f"Subject: {item['Subject']}")
        print(f"Engagement Rate: {item['EngagementRate']}")
        print(f"Total Delivered: {item['TotalDelivered']}")
        print()

#end top_5

def filter_by_campaign(dataset, campaign_alias):
    upper_alias = campaign_alias.upper()

    matching_campaigns = []

    for row in dataset:
        campaign_name = row["Campaign"]
        if upper_alias in campaign_name.upper():
            matching_campaigns.append(row)
    
    return matching_campaigns