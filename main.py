import sys
# from pprint import pprint
import data, get_def, email_args


def main():
    args = email_args.handle_cli_args()

    file_path = args.file_path
    dataset = data.read_email_data(file_path)
    total_rows = get_def.get_total_rows_in_data(dataset)

    if args.all:
        campaign_count = 0

        for i in range(1,total_rows):
            data_row = dataset[i]
            campaign_name = data_row["Campaign"]
            campaign_subject = data_row["Subject"]
            print(f"{i}: {campaign_name}")
            print()
            campaign_count += 1
        print(f"Campaign Count: {campaign_count}")
    
    if args.best:
        print("Test BEST")
    
    if args.top is not None:
        print("Test TOP")
    
    if args.campaign:
        print("Filtering by campaign")


if __name__ == "__main__":
    main()