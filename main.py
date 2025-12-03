import sys
import csv


def main():
    if len(sys.argv) < 2:
        print("Usage: Python3 main.py <file_path>")
        sys.exit(1)

    with open('csv-files/test.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(','.join(row))


main()