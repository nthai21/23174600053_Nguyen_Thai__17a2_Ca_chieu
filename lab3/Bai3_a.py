''' In ra các số nguyên tố từ 100 đến 1000 (kể cả số 1000)
Số nguyên tố: Là các số lớn hơn 1 và chỉ có hai ước là 1 và chính nó. Ví dụ: 2, 3,
5, 7, 11, 13, .'''
print("Các số nguyên tố từ 100 đến 1000 là:")
for i in range(100, 1001):
    if i > 1:
        so = True
        for a in range(2, int(i ** 0.5) + 1):
            if i % a == 0:
                so = False
                break
        if so:
            print(i, end=" ")