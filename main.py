import csv
from utils.openspace import An_Open_Space

# Function to read names from CSV
def read_names_from_csv(filepath):
    """Read names from a CSV file (one name per line)."""
    names = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # skip empty rows
                names.append(row[0])
    return names

def main():
    input_filepath = "data/new_colleagues.csv"
    output_filename = "data/output.csv"

    # Read names from CSV
    names = read_names_from_csv(input_filepath)

    # Create an Open Space with 6 tables of 4 seats
    open_space = An_Open_Space(number_of_tables=6, table_capacity=4)

    # Assign colleagues randomly to tables
    open_space.organize(names)

    # Save the seating plan to CSV
    open_space.store(output_filename)

    # Display the plan in the terminal
    open_space.display()

if __name__ == "__main__":
    main()