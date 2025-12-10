import sys
# from pprint import pprint
import data, get_def, email_args


def main():
    args = email_args.handle_cli_args()

    file_path = args.file_path
    dataset = data.read_email_data(file_path)

    if args.campaign:
        dataset = data.filter_by_campaign(dataset,args.campaign)

    if args.all:
        for row in dataset:
            campaign_name = get_def.get_campaign(dataset,row)
            total_opens = get_def.get_totalOpens(dataset, row)
            print(f"{row}: {campaign_name}")
            print(f"Total Opens: {total_opens}")
            print()
    
    if args.best:
        best_performing_email = get_def.get_best_performer(dataset)
        print(best_performing_email)
    
    if args.top is not None:
        dataset = data.calculate_top_five(dataset,args.top)
    
    if args.worst:
        print("Test WORST")

    
    print_data(dataset)

def print_data(dataset):
    for row in dataset:
        print(f"Campaign: {row["Campaign"]}")
        print(f"Engagement Rate: {row["EngagementRate"]}")
        print()


if __name__ == "__main__":
    main()