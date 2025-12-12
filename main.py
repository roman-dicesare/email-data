import sys
# from pprint import pprint
import data, email_args


def main():
    args = email_args.handle_cli_args()

    file_path = args.file_path
    dataset = data.read_email_data(file_path)
    
    if args.campaign:
        dataset = data.filter_by_campaign(dataset,args.campaign)
    
    if args.top is not None:
        dataset = data.calculate_top_five(dataset,args.top)
    
    if args.worst:
        dataset = data.calculcate_worst(dataset)

    data.print_data(dataset)
    #end main()


if __name__ == "__main__":
    main()