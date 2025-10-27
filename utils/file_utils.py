import csv
def read_names_from_csv(filepath):
    names = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:  # uses the filepath 
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # skip empty rows
                names.append(row[0])
    return names