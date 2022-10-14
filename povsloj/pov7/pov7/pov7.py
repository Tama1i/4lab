y = float(input("enter ugol chasovoi"))
# hour = 30 degree, 1 minute = 0.5 degree, 1second = 0.083 degree

#dg = (h * 30) + (m * 0.5) + (s * 0.083)
h = y // 30
m = (y % 30) // 0.5
s = ((y % 30) % 0.5) // 0.083
o1 = (m*6) + (s * 0.1)
print("ugol dla min strekki ",o1, " polnih chasov ",h, " polnih minut ",m)
