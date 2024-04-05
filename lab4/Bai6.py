'''Viết chương trình nhập một số từ bàn phím và in ra màn hình bằng chữ tiếng
Anh'''
print('-----------------------------------Bài làm--------------------------')
from num2words import num2words
a=int(input("Nhập vào số bất kỳ:"))
trans=num2words(a,lang='en')
print("Số",a,':',trans)


