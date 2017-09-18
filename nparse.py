import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    # open CSV file
    opened_file = open(raw_file)

    # read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    #Build a data structure to return parsed data
    parsed_data =[]

    #skip over the first line of the csv file and store it as fields
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # close CSV file
    opened_file.close()

    return parsed_data


def main():
    new_data = parse(MY_FILE, ",")

    print new_data

if __name__ == "__main__":
    main()
