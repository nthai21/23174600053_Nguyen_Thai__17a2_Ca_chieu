canh_day=float(input("Mời nhập vào độ dài cạnh đáy :"))
chieu_cao=float(input("Mời nhập vào độ dài chiều cao :"))
sxq=4*0.5*canh_day*chieu_cao
stp=sxq+canh_day**4
V=1/3*canh_day**2*chieu_cao
print("Diện tích xung quanh của hình chóp tứ giác đều là :",round(sxq,2))
print("Diện tích toàn phần hình chóp tứ giác đều là :",round(stp,2))
print("Thể tích toàn phần hình chóp tứ giác đề là :",round(V,2))