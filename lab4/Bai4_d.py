print('----------------------------Bài làm-------------------------')
n=int(input("Nhập vào giá trị n>10:"))
a=1
tong=0
while True:
    tong+=a*(a+1)*(a+2)
    if a>n:
        break
    a+=1
print("Tổng giá trị là:",tong)