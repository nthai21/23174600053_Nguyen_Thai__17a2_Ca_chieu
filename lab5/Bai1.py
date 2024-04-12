'''Viết một chương trình Python nhận đầu vào là một số nguyên dương (số thập
phân), và sau đó chuyển đổi nó sang số nhị phân.'''
print('----------------------------------Bài làm-----------------------------------')
a = int(input("Nhập một số nguyên dương (số thập phân): "))

# Khởi tạo một chuỗi rỗng để lưu trữ số nhị phân
nhi_phan = ""

while a > 0:
    du = a % 2
    nhi_phan = str(du) + nhi_phan
    a = a // 2

# In ra kết quả
print("Số nhị phân tương ứng là:", nhi_phan)
