'''Tạo một từ điển (tên từ điển là tên của sinh viên), với từ điển là các phần tử mà
có key là x và value của key là x3. Hãy viết chương trình nhập vào một số
nguyên N và in ra từ điển dạng như trên với độ dài bằng N'''
print('-------------------------------Bài làm-----------------------------')
# Nhập số nguyên N từ người dùng
N = int(input("Nhập số nguyên N: "))

# Tạo từ điển với key là các số từ 1 đến N và value là bình phương của key
tu_dien = {}
for i in range(1, N+1):
    tu_dien[i] = i ** 3

# In ra từ điển đã tạo
print("Từ điển:")
for key, value in tu_dien.items():
    print(key, "->", value)
