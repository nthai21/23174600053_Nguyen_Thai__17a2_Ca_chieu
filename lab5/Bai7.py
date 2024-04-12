'''Viết một chương trình Python để đếm số lượng chữ thường, chữ hoa, chữ số
và ký tự đặc biệt trong một chuỗi đã ch0'''
print('--------------Bài làm---------------')
string = input("Nhập vào một chuỗi: ")
chu_thuong = 0
chu_hoa = 0
chu_so = 0
ky_tu = 0

for char in string:
    if char.islower():
            chu_thuong += 1
    elif char.isupper():
            chu_hoa += 1
    elif char.isdigit():
            chu_so += 1
    else:
            ky_tu += 1
print("Số lượng chữ thường:", chu_thuong)
print("Số lượng chữ hoa:", chu_hoa)
print("Số lượng chữ số:", chu_so)
print("Số lượng ký tự đặc biệt:", ky_tu)
