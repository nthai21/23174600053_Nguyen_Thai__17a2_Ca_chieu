'''Viết chương trình in ra các số chính phương nhỏ hơn 100 (sử dụng vòng lặp
while)'''
print("------------------------------Bài làm-------------------------")
n=1
while n <100:
    can = 1
    dieu_kien = False
    while can * can <= n:
        if can * can == n:
            dieu_kien = True
            break
        can += 1
    if dieu_kien:
        print(n,end=",")
    n += 1