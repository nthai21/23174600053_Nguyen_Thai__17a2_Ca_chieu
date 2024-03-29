n=int(input("Mời nhập giá trị của n:"))
while n <= 0:
    n = int(input("Nhập một số nguyên dương n: "))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum-=1/i
    else:
        sum+=1/i
print("Tổng giá trị từ 1-n:",sum)