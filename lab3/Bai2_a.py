''' Viết chương trình để tính tổng các số chia hết cho 7 nhưng không chia hết
cho 5 trong khoảng từ 2000 đến 4000'''
sum=0
for i in range(2000,4000+1):
    if i%7==0 and i%5!=0:
        sum+=i
print("Tổng số từ 2000-4000 chia hết cho 7 nhưng không chia hết cho 5 là:",sum) 