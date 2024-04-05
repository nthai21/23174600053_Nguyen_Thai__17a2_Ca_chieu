'''Viết chương trình để in ra tất cả các số Fibonacci nhỏ hơn 1000 (sử dụng vòng
lặp while)'''
print('--------------------Bài làm-------------------')
print("Các số Fibonacci nhỏ hơn 1000 là:")
so_truoc = 0
so_hien_tai = 1
while so_hien_tai < 1000:
    print(so_hien_tai, end=",")
    so_sau_cong = so_truoc + so_hien_tai
    so_truoc = so_hien_tai
    so_hien_tai = so_sau_cong
