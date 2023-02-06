# this code is about how to basically copy paste the document.
with open("file3.txt",'r') as rf:
    with open("file4.txt",'w') as wf:
        wf.write(rf.read())