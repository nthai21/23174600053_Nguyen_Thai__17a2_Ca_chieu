print("----------------------Bài làm-------------------------")
n=int(input("Nhập giá trị n>10:"))
a=1
tong=0
while True:
    tong+=1/(3*(2*a+1))
    if a>n:
        break
    a+=1
print("Tổng giá trị là :",tong)