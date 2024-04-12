'''Viết chương trình yêu cầu người dùng nhập một chuỗi văn bản và từ cần tìm
kiếm. Sau đó, hiển thị vị trí (index) của từ đó trong chuỗi và kiểm tra xem từ
nào xuất hiện nhiều nhất trong chuỗi sau đó hiển thị kết quả.'''
print('--------------------------------Bài làm------------------------------')
chuoi_van_ban = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = chuoi_van_ban.find(tu_can_tim)
tu_nhieu_nhat = max(chuoi_van_ban.split(), key=chuoi_van_ban.split().count)
if vi_tri != -1:
    print("Vị trí của từ trong chuỗi là:", vi_tri)
else:
    print("Từ không xuất hiện trong chuỗi.")
print("Từ xuất hiện nhiều nhất trong chuỗi là:", tu_nhieu_nhat)
