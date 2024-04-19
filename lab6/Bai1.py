'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một mảng gồm n số nguyên dương từ bàn
phím.
+ Phân loại và tính tổng:
Tính tổng của tất cả các số chẵn trong mảng.
Tính tổng của tất cả các số lẻ trong mảng.
Xuất hai kết quả trên ra màn hình'''
print('---------------------------------Bài làm---------------------------------')
# Nhập số phần tử của mảng
n = int(input("Nhập số phần tử của mảng: "))
hehe = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    hehe.append(num)
tong_chan = 0
tong_le = 0
for num in hehe:
    if num % 2 == 0:
        tong_chan += num
    else:
        tong_le += num

# In kết quả ra màn hình
print("Tổng các số chẵn trong mảng là:", tong_chan)
print("Tổng các số lẻ trong mảng là:", tong_le)



