fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.split()
    
    for word in words:
        lst.append(word)

lst.sort()
print(list(dict.fromkeys(lst)))

#print(line.rstrip())