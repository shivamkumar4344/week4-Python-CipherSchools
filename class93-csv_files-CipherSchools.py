#CSV :- CSV files are files which are used to represent the data in tabular form.

from csv import reader
with open("file.csv",'r') as f:
    csv_reader = reader(f)
    for r in csv_reader:
        print(r)
    