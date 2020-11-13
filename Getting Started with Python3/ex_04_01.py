def computepay(h,r):
	if h <= 40:
		p = h*r

	if h > 40:
		x = 40*r
		y = 1.5*r*(h-40)
		p = x+y
	return p


hrs = input("Enter Hours:")
rate = input ("Enter Rate:")

h = float(hrs)
r = float(rate)


p = computepay(h,r)
print("Pay",p)
