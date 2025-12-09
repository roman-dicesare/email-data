import argparse

def handle_cli_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a","--all",
                        action="store_true",
                        help="Show ALL emails")
    