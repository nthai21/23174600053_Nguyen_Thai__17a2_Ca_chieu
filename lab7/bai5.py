'''Khai báo 2 từ điển dưới đây:
kho = {
"banana": 6,
"apple": 5,
"orange": 32,
"pear": 15
} g
ia_tien = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
} T
ính hóa đơn khi mua đồ ở cửa hàng trên. Trên hóa đơn mua hàng bao gồm
các thông tin:
+ Mặt hàng đã mua
+ Số lượng mặt hàng đã mua
+ Đơn giá của từng mặt hàng'''
print('-------------------------Bài làm-----------------------')
# Khai báo từ điển cho kho hàng và giá tiền
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Tính tổng số lượng mặt hàng đã mua và tổng tiền
tong_so_luong = 0
tong_tien = 0

# In hóa đơn
print("Hóa đơn mua hàng:")
print("------------------")
for mat_hang, so_luong in kho.items():
    don_gia = gia_tien[mat_hang]
    tong_so_luong += so_luong
    tong_tien += so_luong * don_gia
    print("{}: {} x {} = {}".format(mat_hang, so_luong, don_gia, so_luong * don_gia))

print("------------------")
print("Tổng số lượng: {}".format(tong_so_luong))
print("Tổng tiền: {}".format(tong_tien))

