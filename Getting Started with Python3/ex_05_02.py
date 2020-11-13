largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp) #float로 하면 소수점이 나와서 int로 변경
    except ValueError: #and not all errors!
        print ("Invalid input")
    else:
        # This block will execute if no exception is caught.
        # Yes, this is valid python.
        if smallest is None: #first number!
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print ("Maximum is", largest)
print ("Minimum is", smallest)
