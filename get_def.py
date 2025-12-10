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