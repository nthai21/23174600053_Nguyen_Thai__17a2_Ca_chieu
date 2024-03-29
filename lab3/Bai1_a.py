#S1=1+2+3...+n
n=int(input("Mời nhập giá trị của n:"))
while n <= 0:
    n = int(input("Nhập một số nguyên dương n: "))
# Tính tổng S_n
sum_n = 0
for i in range(1, n + 1):
    sum_n += i

print("Tổng S_n =", sum_n)



   