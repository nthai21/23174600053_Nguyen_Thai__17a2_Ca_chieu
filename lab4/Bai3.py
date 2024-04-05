'''Viết chương trình nhập vào một số nguyên và in ra số chữ số của số nguyên đó
(sử dụng vòng lặp while)'''
print('---------------------Bài làm--------------------')
n=int(input("Mời nhập vào số nguyên :"))
dem=0
while n!=0:
    dem+=1
    n//=10
print("Số chữ số là:",dem)


