import sys
# from pprint import pprint
import data, get_def

def main():
    file_name = data.handle_argvs()
    dataset = data.open_file(file_name)
    campaign_initial = data.set_campaign_initial()

    print()
    print(f"{file_name} loaded succesfully.")
    print("------------------------")
    print()

    # print(f"TEST: {get_def.get_specific_campaign(dataset,data.set_campaign_initial())}")

    print(get_def.display_same_campaigns(get_def.get_specific_campaign(dataset,campaign_initial)))

    ##end main()##

main()