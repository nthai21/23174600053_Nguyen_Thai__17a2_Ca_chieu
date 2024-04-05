print("-----------------------Bài làm------------------")
n = int(input("Nhập vào số nguyên n>10: "))
a = 1
tong = 0
while True:
    tong+=6**a
    if a > n:
        break
    a += 1
print("Tổng giá trị là :",tong)



