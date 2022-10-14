a1 = int(input("a1"))
a2 = int (input("a2"))
a3 = int (input("a3"))
b1 = int (input("b1"))
b2 = int (input("b2"))

ch3 = a3 + ((a2+b2 + (a1+b1)//10) // 10)
ch2 = (a2 + b2 + (a1 + b1) // 10) % 10
ch1 = (a1 + b1) % 10

print(ch3, ch2, ch1)
