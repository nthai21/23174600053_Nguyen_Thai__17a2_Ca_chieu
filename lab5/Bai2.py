
'''Viết một chương trình Python nhận đầu vào là hai chuỗi ký tự str1 và str2, sau
đó tìm ra chuỗi ký tự con chung có độ dài ngắn nhất của hai chuỗi này'''
print('--------------------Bài làm-------------------')
# Nhận đầu vào từ người dùng
str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

# Tìm chiều dài của hai chuỗi
len_str1 = len(str1)
len_str2 = len(str2)

# Khởi tạo một ma trận để lưu trữ độ dài của chuỗi con chung
dodai_chuoi_con_chung = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

# Tìm độ dài của chuỗi con chung ngắn nhất
do_dai_ngan_nhat = 0
for i in range(1, len_str1 + 1):
    for j in range(1, len_str2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dodai_chuoi_con_chung[i][j] = dodai_chuoi_con_chung[i - 1][j - 1] + 1
            do_dai_ngan_nhat = max(do_dai_ngan_nhat, dodai_chuoi_con_chung[i][j])

# Tìm chuỗi con chung ngắn nhất
chuoi_con_chung_ngan_nhat = ""
for i in range(len_str1):
    for j in range(len_str2):
        if dodai_chuoi_con_chung[i + 1][j + 1] == do_dai_ngan_nhat:
            chuoi_con_chung = str1[i - do_dai_ngan_nhat + 1: i + 1]
            if chuoi_con_chung not in chuoi_con_chung_ngan_nhat:
                chuoi_con_chung_ngan_nhat = chuoi_con_chung

# In ra kết quả
if chuoi_con_chung_ngan_nhat:
    print("Chuỗi ký tự con chung ngắn nhất là:", chuoi_con_chung_ngan_nhat)
else:
    print("Không có chuỗi ký tự con chung nào.")

