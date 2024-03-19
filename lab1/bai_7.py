import math

a1 = int(input("Nhap a1: "))
b1 = int(input("Nhap b1: "))
c1 = int(input("Nhap c1: "))

print("__________")

a2 = int(input("Nhap a2: "))
b2 = int(input("Nhap b2: "))
c2 = int(input("Nhap c2:  "))

print("Phuong trinh")

print(a1,"x X + ",b1, "x Y", " = ", c1)
print(a2,"x X + ",b2, "x Y", " = ", c2)

print("Ket qua")

x = round((b1*c2 - b2*c1) / (a1*b2 - a2*b1))
y = round((c1*a2 - c2*a1) / (a1*b2 - a2*b1))

print("Phuong trinh co nghiem X = ", str(x))
print("Phuong trinh co nghiem Y = ", str(y))
