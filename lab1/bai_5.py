gio_su_dung=float(input("Mời nhập vào số giờ tiêu thụ điện :"))
nang_luong_tieu_thu = gio_su_dung * 220 * 1.5 / 1000
    
# Giá điện (đồng/kWh)
gia_dien = 5000
    
    # Tính tổng số tiền điện phải trả
tien_dien = nang_luong_tieu_thu * gia_dien
print("Số tiền điện gia chủ phải trả là :",tien_dien)
  