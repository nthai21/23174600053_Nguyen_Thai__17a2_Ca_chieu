'''Viết một chương trình Python để xóa tất cả các khoảng trắng giữa các ký tự
trong một chuỗi đã cho'''
print('------------------Bài làm--------------------------')
chuoi = input("Nhập chuỗi: ")

    # Tạo một chuỗi mới không chứa khoảng trắng
chuoi_moi = ""
for char in chuoi:
        if char != " ":
            chuoi_moi += char

    # Hiển thị kết quả
print("Chuỗi sau khi xóa khoảng trắng:", chuoi_moi)
