#Sn=1/2+1/3+1/4+...+1/n
n=int(input("Mời nhập giá trị của n:"))
while n <= 0:
    n = int(input("Nhập một số nguyên dương n: "))
sum=0
for i in range(1,n+1):
    sum+=1/i
print("Tổng từ 1-1/n:",sum)


