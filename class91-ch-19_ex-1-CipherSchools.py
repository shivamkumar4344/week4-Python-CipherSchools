# output should be in the manner of :-
# Raman's salary is 100000
# Kunal's salary is 120000

with open("salary.txt",'r') as rf:
    with open("solution.txt",'a') as wf:
        for lines in rf.readlines():
            name,salary = lines.split(',')
            wf.write(f"{name}'s salary is {salary}")     