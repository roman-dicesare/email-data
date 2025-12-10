import argparse

def handle_cli_args():
    parser = argparse.ArgumentParser(description="Analyze email data")

    parser.add_argument(
        "file_path",
        type=str,
        help="Path to the CSV file you want to analyze"
    )

    parser.add_argument("-c","--campaign",
                        type=str,
                        help="Filter results by campaign initial (optional)")

    parser.add_argument("-a","--all",
                        action="store_true",
                        help="Show ALL emails")
    
    parser.add_argument("-t","--top",
                        type=int,
                        nargs="?",
                        const=5,
                        help="Show top N emails (default 5.)")
    
    parser.add_argument("-w","--worst",
                        action="store_true",
                        help="Show worst-performing email data")
    
    return parser.parse_args()