# Use words.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)
inp = fhand.read()

for line in fhand:
    line = line.rstrip()
    prt = line.upper()
    print(prt)