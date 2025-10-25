import random 
from utils.table import Table
class An_Open_Space :
    def __init__(self, number_of_tables:int,table_capacity :int):    # if (6,4)
        self.tables=[]# This is a list of Table objects.
        self.number_of_tables=number_of_tables
        for i in range(number_of_tables):
            self.tables.append(Table(capacity=table_capacity)) # if (6,4) self.tables = [Table(4), Table(4), Table(4),Table(4),Table(4), Table(4)]

    def organize(self, names:list): #that will:randomly assign people to Seat objects in the different Table objects.
        for name in names : # For each person  check which tables have free spots
            free_tables = []
            for table in self.tables: 
               if table.has_free_spot(): #  check free spot in the table 
                  free_tables.append(table) # add the table with free spot in the list free_table
            if not free_tables:   # If free_tables is empty, that means there are no seats left for the current person.
               print(f"No free seats available for {name}")
            else:
                chosen_table = random.choice(free_tables) # Picks a table randomly from free_table list 
                chosen_table.assign_seat(name) # places the name  at the table

    def display(self): #display the different tables and there occupants in a nice and readable waystore
        table_number = 1
        for table in self.tables:
            print(f"\nTable {table_number}:")
            seat_number = 1
            for seat in table.seats:
                if seat.free:
                    print(f"  Seat {seat_number}: Free")
                else:
                    print(f"  Seat {seat_number}: Occupied by {seat.occupant}")
                seat_number += 1
            table_number += 1

    def store(self, filename="data/output.csv"): #Store the seating arrangement in a CSV file
        import csv  # now we actually use it

        with open(filename, "w", newline="", encoding="utf-8") as f: # Create a CSV writer object to write rows to the file
    
            writer = csv.writer(f) # Write a header row
            writer.writerow(["Table Number", "Seat Number", "Occupant"])

            table_number = 1       # Initialize table numbering starting from 1
            for table in self.tables:  # Loop through each Table object in the OpenSpace
                seat_number = 1
                for seat in table.seats: # Loop through each Seat object in the current Table
                    occupant = seat.occupant if not seat.free else "Free" # If the seat is free, mark "Free"; otherwise, write the occupant's name
                    writer.writerow([table_number, seat_number, occupant])# Write a row in the CSV file: table number, seat number, occupant/free
                    seat_number += 1 # Increment seat number for the next seat
                table_number += 1  # Increment table number for the next table