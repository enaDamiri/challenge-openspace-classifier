Description
Your company moved to a new office. It's an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues.
![alt text](image.png)
You will create a program that runs everyday to re-assign everybody to a new seat.
We want to create a program that assigns 24 people to 6 tables in an openspace. Before getting started, take inventory what do we need:

Project Structure
challenge-openspace-classifier/
├── data/
│ ├── new_colleagues.csv # list of colleague names (input)
│ └── output.csv # seating plan output
├── utils/
│ ├── file_utils.py # helper functions for reading CSV
│ ├── openspace.py # main OpenSpace logic
│ └── table.py # Seat and Table classes
├── main.py # script entry point
└── README.md



Installation
Python 3.x installed on your system
No external libraries needed (uses standard `csv` and `random` modules)

1. Clone the repository:
```bash
#git clone <repository_url>
2. Navigate into the project folder:
```bash
#cd challenge-openspace-classifier

Usage
Run the script from the project root:
python main.py


(Visuals)
Example Terminal Output
Table 1:
  Seat 1: Aleksei
  Seat 2: Amine
  Seat 3: Free
  Seat 4: Anna

Table 2:
  Seat 1: Astha
  Seat 2: Brigitta
  Seat 3: Bryan
  Seat 4: Free
...
(Contributors)
[Ena Damiri] – Project creator & developer

(Timeline)
This project was completed in two days as part of the AI Bootcamp at BeCode.org.

(Personal situation)
This project was done as part of a learning exercise to practice Python classes, CSV handling, and file management.
It helps understand object-oriented programming and practical file utilities for real-world scenarios.

( Features)
- **Randomized Seating:** Each run assigns colleagues to different seats randomly.  
- **CSV Output:** Seating plan is saved in a CSV file for easy tracking.  
- **Terminal Display:** Prints the seating plan in a readable format in the terminal.  
- **Seat Availability Check:** Automatically detects if a table or seat is full.

(Additional Feature)
- **Dynamic Configuration:** While the office has 6 tables of 4 seats, the code allows you to create **any number of tables and seats** by changing the parameters in `An_Open_Space`.  
