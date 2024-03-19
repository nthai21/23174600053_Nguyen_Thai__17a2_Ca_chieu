#Có 50 viên bi:20 đỏ,15 xanh,15 vàng
import math
a=int(input("Mời nhập vào số bi cần lấy :"))
print("Xác suất để lấy toàn bi đỏ là :",math.comb(20,a)/50)
#Lấy ít nhất có một viên bi xanh 
print("Xác suất để lấy có ít nhất 1 viên bi xanh là:",math.comb(15,a)*math.comd(20,a-1)/50)


   


