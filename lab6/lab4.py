'''Viết một chương trình Python để thực hiện các yêu cầu sau:
a) Dãy Fibonacci:
Tạo một danh sách chứa n số Fibonacci đầu tiên, trong đó n được người dùng
nhập từ bàn phím.
Yêu cầu: Sử dụng list comprehension để tạo danh sách này.
b) Danh sách số nguyên tố:
Tạo một danh sách chứa tất cả các số nguyên tố nhỏ hơn 100.
Yêu cầu: Sử dụng list comprehension để tạo danh sách này'''
print('----------------------------Bài làm-------------------------------')
# a) Dãy Fibonacci
n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))

fibonacci = [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, n)]

print("Danh sách {} số Fibonacci đầu tiên:".format(n))
print(fibonacci)

# b) Danh sách số nguyên tố
so_nguyen_to = [x for x in range(2, 100) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

print("Danh sách các số nguyên tố nhỏ hơn 100:")
print(so_nguyen_to)






