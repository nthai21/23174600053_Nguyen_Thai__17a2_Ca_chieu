'''  Viết chương trình để tính tổng các số chia hết cho 4 nhưng không chia hết
cho 6 trong khoảng từ 500 đến 1000.'''
sum=0
for i in range(500,1001):
    if i%4==0 and i%6!=0:
        sum+=i
print("Tổng số chia hết cho 4 nhưng không chia hết cho 6 là :",sum)