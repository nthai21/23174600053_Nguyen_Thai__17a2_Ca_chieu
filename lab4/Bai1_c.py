'''Viết chương trình nhập vào các số nguyên dương từ bàn phím cho đến khi tổng
các số đã nhập vượt quá 1000. Sau đó in ra màn hình:
a) Đếm số nguyên dương vừa nhập'''
print("----------------------------Bài làm-------------------------")
dem = 0
tong = 0
while tong <= 1000:
        n = int(input("Nhập số nguyên dương: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương.")
            continue
        dem += 1
        tong += n
    # In ra số lượng số nguyên dương đã nhập
print("Số nguyên dương đã nhập là:", dem)

