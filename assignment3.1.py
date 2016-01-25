hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
h = float(hrs)
r = float(rate)
if h < 40:
    print(h * r)
else:
    print(40 * r + (h - 40) * 1.5 * r)
