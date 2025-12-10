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

def calculate_top_five(dataset, total_rows):
    scored_rows = []

    for i in range(0,total_rows):
        data_row = dataset[i]
        engagement_rate = (data_row["EngagementRate"]).strip(" %")
        scored_rows.append({"Campaign": data_row["Campaign"],
                            "Subject" : data_row["Subject"], 
                            "Engagement Rate" : float(engagement_rate),
                            "TotalDelivered" : data_row["TotalDelivered"]})
    
    sorted_rows = sorted(scored_rows, key = lambda row: row["Engagement Rate"], reverse = True)

    top_five = sorted_rows[:5]

    return top_five

def print_top_five_emails(dataset,total_rows):
    top_five_rates = calculate_top_five(dataset,total_rows)
    print("Top 5 email campaigns:")
    print("-----")
    for item in top_five_rates:
        print(f"Campaign Name: {item['Campaign']}")
        print(f"Subject: {item['Subject']}")
        print(f"Engagement Rate: {item['Engagement Rate']}")
        print(f"Total Delivered: {item['TotalDelivered']}")
        print()

#end top_5