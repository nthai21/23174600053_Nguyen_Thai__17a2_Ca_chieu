'''Viết chương trình sử dụng kiến thức về từ điển nhập từ bàn phím thông tin của
10 sinh viên, bao gồm: tên và điểm thi. Yêu cầu:
1. Xếp loại học lực của sinh viên theo điểm thi:
+ Điểm dưới 4.0: F
+ Điểm từ 4.0 đến 5.4: D
+ Điểm từ 5.5 đến 6.9: C
+ Điểm từ 7.0 đến 8.4: B
+ Điểm từ 8.5 đến 10.0: A
2. Thống kê số lượng sinh viên ở mỗi loại học lực.'''
print('---------------------Bài làm-------------------')
# Khởi tạo từ điển để lưu thông tin của 10 sinh viên
sinh_vien = {}

# Nhập thông tin của 10 sinh viên từ bàn phím
for i in range(10):
    ten = input("Nhập tên của sinh viên {}: ".format(i+1))
    diem_thi = float(input("Nhập điểm thi của sinh viên {}: ".format(i+1)))
    sinh_vien[ten] = diem_thi

# Tạo từ điển để lưu thông tin xếp loại học lực và số lượng sinh viên ở mỗi loại
xep_loai = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for ten, diem_thi in sinh_vien.items():
    if diem_thi >= 8.5:
        xep_loai['A'] += 1
    elif diem_thi >= 7.0:
        xep_loai['B'] += 1
    elif diem_thi >= 5.5:
        xep_loai['C'] += 1
    elif diem_thi >= 4.0:
        xep_loai['D'] += 1
    else:
        xep_loai['F'] += 1

# In ra thông tin số lượng sinh viên ở mỗi loại học lực
print("Thống kê số lượng sinh viên ở mỗi loại học lực:")
for xep_loai, so_luong in xep_loai.items():
    print("Xếp loại {}: {} sinh viên".format(xep_loai, so_luong))
