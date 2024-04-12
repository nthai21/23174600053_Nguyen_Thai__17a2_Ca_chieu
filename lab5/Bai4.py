'''Viết một chương trình Python để loại bỏ tất cả các ký tự không phải là số khỏi
một chuỗi ký tự đã cho. Sau đó, kiểm tra xem chuỗi ký tự kết quả có phải là một
số nguyên tố không và hiển thị kết quả cho người dùng.'''
print('--------------------------Bài làm-------------------------')
chuoi=input("Mời nhập vào chuỗi ký tự:")
so=' '
for i in chuoi:
    if i.isdigit():
        so+=i
if so:
    n=int(so)
    if n<=1:
        check = False
    else:
        check=True
        for j in range(2,n):
            if n%j==0:
                check=False
                break
        if check == True:
            print(n,"Là số nguyên tố.")
            n+=1
        else:
            print(n,"Không phải là số nguyên tố.")
else:
    print("Chuỗi số không chưa bất kỳ số nào.")