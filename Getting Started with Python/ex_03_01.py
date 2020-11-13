hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h <= 40:
    x = (h*r)
    print(x)

if h > 40:
    x = 40*r
    y = 1.5*r*(h-40)
    print(x+y)
