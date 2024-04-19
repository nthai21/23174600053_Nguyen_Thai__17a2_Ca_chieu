'''Viết một chương trình Python để thực hiện các thao tác sau:
+ Cho phép người dùng nhập vào một mảng gồm n số nguyên dương từ bàn
phím.
+ Tìm và in ra màn hình tất cả các số nguyên tố trong mảng đó.
+ Tìm và in ra màn hình tất cả các số hoàn hảo trong mảng đó'''
print('-----------------------------Bài làm----------------------------')
n = int(input("Nhập số phần tử của mảng: "))
arr = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

# Tìm và in ra tất cả các số nguyên tố trong mảng
print("Các số nguyên tố trong mảng là:")
for num in arr:
    if num < 2:  # Số nguyên tố phải lớn hơn 1
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Tìm và in ra tất cả các số hoàn hảo trong mảng
print("Các số hoàn hảo trong mảng là:")
for num in arr:
    if num < 2:  # Số hoàn hảo phải lớn hơn 1
        continue
    divisor_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i
    if divisor_sum == num:
        print(num)

