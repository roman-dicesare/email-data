import sys
# from pprint import pprint
import data, get_def, email_args


def main():
    args = email_args.handle_cli_args()

    file_path = args.file_path
    dataset = data.read_email_data(file_path)
    total_rows = get_def.get_total_rows_in_data(dataset)

    if args.all:
        for i in range(1,total_rows):
            campaign_name = get_def.get_campaign(dataset,i)
            total_opens = get_def.get_totalOpens(dataset, i)
            print(f"{i}: {campaign_name}")
            print(f"Total Opens: {total_opens}")
            print()
    
    if args.best:
        best_performing_email = get_def.get_best_performer(dataset)
        print(best_performing_email)
    
    if args.top is not None:
        print()
        data.print_top_five_emails(dataset,total_rows)

    if args.campaign:
        print("Filtering by campaign")
    
    if args.worst:
        print("Test WORST")


if __name__ == "__main__":
    main()