'''
Viết một chương trình Python để trộn hai chuỗi ký tự theo quy tắc sau:
+ Lần lượt từ trái sang phải, viết các ký tự của chuỗi đầu tiên, sau đó đến chuỗi
thứ hai.
+ Thêm một dấu gạch nối '-' giữa các ký tự của hai chuỗi'''
print('-------------------------------------Bài làm------------------------')

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

if str1 and str2:
    # Tạo biến kết quả là chuỗi rỗng
    kq = ""

    # Tính độ dài của chuỗi ngắn hơn
    do_dai_min = min(len(str1), len(str2))

    # Trộn các ký tự từ cả hai chuỗi
    for i in range(do_dai_min):
        kq += str1[i] + '-' + str2[i] + '-'

    # Thêm phần còn lại của chuỗi dài hơn vào chuỗi kết quả
    if len(str1) > len(str2):
        kq += str1[do_dai_min:]
    elif len(str2) > len(str1):
        kq += str2[do_dai_min:]

    # Xóa dấu gạch nối cuối cùng nếu có
    if kq.endswith('-'):
        kq = kq[:-1]

    print("Chuỗi sau khi trộn:", kq)
else:
    print("Ít nhất một trong hai chuỗi là rỗng.")
