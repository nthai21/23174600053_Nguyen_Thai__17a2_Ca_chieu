def factorial(n):
    """Tính giai thừa của một số nguyên n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutation(n, r):
    """Tính số hoán vị P(n, r)"""
    return factorial(n) // factorial(n - r)

def combination(n, r):
    """Tính số tổ hợp C(n, r)"""
    return permutation(n, r) // factorial(r)

# Ví dụ sử dụng các hàm trên
n = int(input('Nhập giá trị của n:'))
r = int(input('Nhập giá trị của r:'))
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: P({n}, {r}) = {permutation(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: C({n}, {r}) = {combination(n, r)}")
