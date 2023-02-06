f = open("file1.txt")
print(f'cursor position- {f.tell()}')
print(f.read())
print(f'cursor position- {f.tell()}')
print(f.seek(2))  #seek method decides the position of cursor.
# readlines -: It read the lines one by one.

lines = f.readlines()
print(len(lines))# It count the number of lines..

#loop in lines
for x in lines:
    print(x,end='')


print("\n",f.name)# it tells the name of the file.
f.close()

