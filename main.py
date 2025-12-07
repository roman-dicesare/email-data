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

    print(f"{file_name} loaded succesfully.")
    print()

    # print(data.get_datetime(dataset, 6)) #how can we eliminate magic numbers here?  
    # print(data.get_campaign(dataset, 6))
    # print(f"Total Opens: {data.get_totalOpens(dataset,6)}")

    # print(f"Engagement Rate: {data.get_engagementRate(dataset,6)}")

    print("------------------------")
    print()
    print(f"Best Performing Email Engagment Rate: {data.get_best_performer(dataset)}")

    ##end main()##

main()