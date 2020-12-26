import re
total = 0

sample = open('11_actual_data.txt')
for line in sample:
    line = line.rstrip()
    y = re.findall('([0-9]+)', line) 

    for num in y:
        value = int(num) 
        total = total + value
print(total)
