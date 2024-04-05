print('----------------------------------Bài làm--------------------------')
n=int(input("Nhập giá trị của n>10:"))
tong=0
a=1
while True:
    tong+=(-1)**a*a**2
    if a>n:
        break
    a+=1
print("Tổng giá trị là :",tong)
    