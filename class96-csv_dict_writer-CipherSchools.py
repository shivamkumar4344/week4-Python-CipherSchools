from csv import DictWriter
with open("file3.csv",'w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    
    csv_writer.writerows([
        {'firstname':'shivam','lastname':'yadav','age':19},
        {'firstname':'raman','lastname':'singh','age':26},
        {'firstname':'samir','lastname':'kumar','age':22}
        
    ])