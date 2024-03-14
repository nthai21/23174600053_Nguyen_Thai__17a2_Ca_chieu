import math
x=int(input("Mời nhập vào giá trị của a:"))
z=int(input("Mời nhập vào giá trị của z:"))
tu=x**2*math.sin(x)+math.sqrt(abs(x))
e=2.718
mau=math.log(z)+e**x-1
tu_mau=tu/mau
fx=tu_mau+math.atan(x*z)
print("Giá trị của biểu thức f(a,z)=",round(fx,2))