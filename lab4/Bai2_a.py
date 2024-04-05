'''Viết chương trình in ra các số nguyên tố nhỏ hơn 100 (sử dụng vòng lặp
while)'''
print("-----------------Bài làm----------------------")
n = 2
while n < 100:
    dieu_kien = True
    so_chia = 2
    while so_chia * so_chia <= n:
        if n % so_chia == 0:
            dieu_kien = False
            break
        so_chia += 1
    if dieu_kien:
        print(n,end=",")
    n += 1