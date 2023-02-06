from csv import writer
with open("file2.csv",'w',newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Shivam','India'])
    csv_writer.writerow(['Alex','England'])
    csv_writer.writerows([['Kumar','Australia'],['Sam','Mexico']])#writerows is used to write multiple rows.