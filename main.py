import sys
import csv
import statistics

def main():
    assert len(sys.argv) > 1, "No input file path specified."
    input_file_path = sys.argv[1]
    print("Processing input file: {input_file_path}")

    with open('example_input.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            numlist = [float(num) for num in line]
            x = statistics.mean(numlist)
            print(x)

if __name__ == "__main__":
    main()
