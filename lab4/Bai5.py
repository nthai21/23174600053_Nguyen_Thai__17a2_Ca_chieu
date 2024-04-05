'''Viết chương trình thực hiện các phép tính số học trên hai số nhập từ người
dùng và cho phép người dùng tiếp tục nếu muốn (sử dụng vòng lặp while).
Yêu cầu:
+ Chương trình yêu cầu người dùng nhập hai số từ bàn phím.
+ Chương trình thực hiện các phép tính cộng, trừ, nhân, chia, lũy thừa và tính
căn bậc hai của hai số này.
+ Sau mỗi phép tính, chương trình hỏi người dùng có muốn tiếp tục không và
chờ đợi phản hồi của người dùng để quyết định tiếp tục hay kết thúc chương
trình.'''
print('--------------------------Bài làm----------------------------')
a=int(input("Nhập giá trị của a:"))
b=int(input("Nhập giá trị của b:"))
import math
while True:
    print("Chọn phép tính:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Lũy thừa")
    print("6. Tính căn bậc hai")
    so = input("Nhập lựa chọn 1;2;3;4;5;6: ")
    if so == '1':
        kq = a + b
        print("Kết quả:", kq)
    elif so == '2':
        kq = a - b
        print("Kết quả:", kq)
    elif so == '3':
        kq = a * b
        print("Kết quả:", kq)
    elif so == '4':
        if a == 0:
            print("Không thể chia cho 0")
        else:
            kq = a / b
            print("Kết quả:", kq)
    elif so == '5':
        result = a ** b
        print("Kết quả:", kq)
    elif so == '6':
        print("Căn bậc hai của số thứ nhất:", math.sqrt(a))
        print("Căn bậc hai của số thứ hai:", math.sqrt(b))
    else:
        print("Lựa chọn không hợp lệ")

    chon = input("Bạn có muốn tiếp tục không?__có or không__: ")
    if chon=="không":
        break


    
