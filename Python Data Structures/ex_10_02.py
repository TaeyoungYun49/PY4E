counts = dict()
handle = open("mbox-short.txt")

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5] 
        hour = time.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)



