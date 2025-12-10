from datetime import datetime
import sys, csv, data

def get_datetime(dataset, row_number):
    data_row = dataset[row_number]
    raw_date = data_row["DateSendStarted"]
    normalized_date : str = data.normalize_DateSendStarted(raw_date)
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
        
        best_performing = (f"{best_performer_campaign} with a {best_performer} engagement rate.")

    return best_performing
    #end

def get_worst_performer(dataset):
    total_rows_in_set = get_total_rows_in_data(dataset)
    worst_performer = dataset[1]["EngagementRate"]
    worst_campaign = ""

    for i in range(1, total_rows_in_set):
        data_row = dataset[i]
        data_in_row = data_row["EngagementRate"]
        data_campaign = data_row["Campaign"]
        if data_in_row < worst_performer:
            worst_performer = data_in_row
            worst_campaign = data_campaign
    return worst_performer, worst_campaign
    #end

def get_specific_campaign(dataset, campaign_initial):
    same_campaigns = []

    total_rows = get_total_rows_in_data(dataset)

    for i in range(1,total_rows):
        data_row = dataset[i]
        campaign_name = data_row["Campaign"]
        if campaign_initial in campaign_name:
            same_campaigns.append(data_row)

    if same_campaigns == []:
        print("That campaign initial wasn't found in this data set. Please try again.")
        print()
        sys.exit(1)
    else:
        return same_campaigns

def display_same_campaigns(same_campaigns):
    for campaign in same_campaigns:
        name = campaign["Campaign"]
        rate = campaign["EngagementRate"]
        print(f"Campaign: {name}")
        print(f"Engagement Rate: {rate}")
        print("---")

#ignore below line. I'm cooking....

def get_top_five_campaigns(dataset):
    top_five = []

    baseline = dataset[1]["EngagementRate"]
    baseline_campaign = dataset[1]["Campaign"]

    total_rows = get_total_rows_in_data(dataset)

    for i in range(1, total_rows):
        data_row = dataset[i]
        data_in_row = data_row["EngagementRate"]
        campaign_name = data_row["Campaign"]

        if data_in_row >= baseline:
            top_five.append(campaign_name,data_in_row)
