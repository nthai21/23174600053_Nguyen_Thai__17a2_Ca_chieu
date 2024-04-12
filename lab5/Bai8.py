# Nhập chuỗi từ người dùng
string = input("Nhập vào một chuỗi có độ dài hơn 10 ký tự: ")

    # Kiểm tra độ dài của chuỗi
if len(string) <= 10:
    print("Chuỗi không đủ độ dài!")
    # a) Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8.
str_a = string[1:8]
print("a) Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", str_a)

    # b) Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5.
str_b = string[4:9]
print("b) Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", str_b)

    # c) Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự.
str_c = string[-3:]
print("c) Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", str_c)

    # d) Chuyển đổi các ký tự trong chuỗi thành chữ thường.
str_thuong = string.lower()
print("d) Chuỗi sau khi chuyển thành chữ thường:", str_thuong)

    # e) Chuyển đổi các ký tự trong chuỗi thành chữ hoa.
str_hoa = string.upper()
print("e) Chuỗi sau khi chuyển thành chữ hoa:", str_hoa)

    # f) Đảo ngược chuỗi ký tự vừa nhập
str_f = string[::-1]
print("f) Chuỗi sau khi đảo ngược:", str_f)