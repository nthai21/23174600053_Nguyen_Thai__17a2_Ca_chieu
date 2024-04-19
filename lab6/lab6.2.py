'''Nhập ma trận vuông: Cho phép người dùng nhập các phần tử của một ma
trận vuông từ bàn phím.
+ Tìm ma trận nghịch đảo: Tìm và xuất ra màn hình ma trận nghịch đảo của ma
trận đã nhập (nếu tồn tại).
+ Kiểm tra xem ma trận đã cho có phải là ma trận đối xứng hay không'''
print('-------------------------------Bài làm---------------------------')
n = int(input("Nhập kích thước của ma trận vuông: "))

# Khởi tạo ma trận vuông và nhập các phần tử từ người dùng
ma_tran_vuong = []
print("Nhập các phần tử của ma trận vuông:")
for i in range(n):
    hang = []
    for j in range(n):