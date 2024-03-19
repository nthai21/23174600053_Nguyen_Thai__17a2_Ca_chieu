''' Viết một chương trình Python cho người dùng có thể lựa chọn các thể loại phim
như Hành động, Kinh dị, Tình cảm, Hài hước và Hoạt hình. Sau đó, yêu cầu
người dùng nhập lựa chọn thể loại phim và thời gian muốn xem phim (sáng,
trưa, chiều, tối). Cuối cùng, chương trình sẽ hiển thị thông báo về thời gian
chiếu phim tương ứng với lựa chọn của người dùng. Hãy lưu ý rằng phim Tình
cảm chỉ được chiếu vào buổi tối, phim hoạt hình chỉ được chiếu vào buổi sáng
và trưa, phim kinh dị chỉ được chiếu vào buổi tối. Nếu thời gian chọn không có
suất chiếu, hãy in ra thông báo "Không có suất chiếu'''
print('--------------------------------Bài làm-----------------------------')
loai_phim=input("Mời quý khách chọn thể loại phim :")
gio_xem=input("Mời quý khách chọn thời gian muốn xem phim:")
if loai_phim=="Hành động" or loai_phim=="Kinh dị" or loai_phim=="Tình cảm"or loai_phim=="Hài hước"or loai_phim=="Hoạt hình":
    if loai_phim=="Hành động" and( gio_xem =="Sáng" or gio_xem=="Chiều" or gio_xem=="Tối"):
        print("""Sáng:8h-12h
                     Chiều:13h-16h
                     Tối:17h-23h""")
    elif loai_phim=="Kinh dị" and gio_xem=="Tối":
        print("Tối :19h-23h")
    elif loai_phim=="Tình cảm" and gio_xem=="Tối":
        print("Tối :19h-23h")
    elif loai_phim=="Hài hước" and( gio_xem =="Sáng" or gio_xem=="Chiều" or gio_xem=="Tối"):
        print("""Sáng:8h-12h
                     Chiều:13h-16h
                     Tối:17h-23h""")
    elif loai_phim=="Hoạt hình" and (gio_xem=="Sáng" or gio_xem=="Chiều"):
        print(""" Sáng 8h-12h
                  Chiều 13h-17h""")
    else:
        print("Không có suất chiếu")
        

        
   