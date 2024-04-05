'''Viết chương trình nhập vào các số nguyên dương từ bàn phím cho đến khi tổng
các số đã nhập vượt quá 1000. Sau đó in ra màn hình:
a) Các số chẵn đã nhập'''
print("-----------------------------------Bài làm--------------------------------")
tong=0
while tong<=1000:
    n=int(input(" Nhập số nguyên dương:"))
    if n<=0:
        print("Vui lòng nhập nguyên dương:")
    elif n%2!=0:
        print("Mời số chẵn")
        continue
    tong+=n
    
    