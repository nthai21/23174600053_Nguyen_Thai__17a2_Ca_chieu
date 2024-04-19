'''
Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một dãy các số nguyên từ bàn phím. Dãy số
có thể chứa bất kỳ số nào.
+ Kiểm tra xem dãy số đó có tạo thành cấp số cộng không.
+ Nếu dãy số tạo thành cấp số cộng, xuất ra màn hình dãy số và thông báo rằng
dãy số này tạo thành cấp số cộng. Nếu không, xuất ra thông báo tương ứng.'''
print('-----------------------------------Bài làm--------------------------------')
danh_sach_so = input("Nhập vào dãy số, cách nhau bằng dấu cách: ").split()

# Chuyển các phần tử trong dãy số thành kiểu số nguyên
danh_sach_so = [int(so) for so in danh_sach_so]

# Kiểm tra xem dãy số có tạo thành cấp số cộng không
la_cap_so_cong = True
buoc_nhay = danh_sach_so[1] - danh_sach_so[0]

for i in range(2, len(danh_sach_so)):
    if danh_sach_so[i] - danh_sach_so[i-1] != buoc_nhay:
        la_cap_so_cong = False
        break
if la_cap_so_cong:
    print("Dãy số {} tạo thành cấp số cộng.".format(danh_sach_so))
else:
    print("Dãy số {} không tạo thành cấp số cộng.".format(danh_sach_so))
