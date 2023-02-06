from csv import DictReader

with open("file.csv",'r') as f:
    csv_read = DictReader(f)
    for x in csv_read:
        print(x)
        print(x['name'])
        print(x['salary'])