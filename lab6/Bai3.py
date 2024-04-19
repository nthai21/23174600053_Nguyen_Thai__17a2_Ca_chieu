'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một dãy các số từ bàn phím. Dãy số có thể
bao gồm bất kỳ số nào, có thể là số nguyên, số thực hoặc cả hai.
+ Tìm và in ra màn hình số lớn nhất và số nhỏ nhất trong dãy số đó.'''
print('----------------------------Bài làm--------------------------')
n = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()

# Khởi tạo biến để lưu trữ số lớn nhất và số nhỏ nhất
so_lon = None
so_nho = None

# Duyệt qua từng số trong dãy và cập nhật số lớn nhất và số nhỏ nhất
for num_str in n:
    # Chuyển đổi số từ dạng chuỗi sang số
    num = float(num_str)
    # Nếu đây là số đầu tiên trong dãy, gán cho cả max_number và min_number
    if so_lon is None or num > so_lon:
       so_lon = num
    if so_nho is None or num < so_nho:
        so_nho = num
print("Số lớn nhất trong dãy là:", so_lon)
print("Số nhỏ nhất trong dãy là:", so_nho)

