def sumPdivisors(n):
    """Tính tổng các ước số chính của số nguyên n, ngoại trừ chính số đó"""
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def is_amicable(a, b):
    """Kiểm tra xem hai số a và b có phải là số amicable hay không"""
    return sumPdivisors(a) == b and sumPdivisors(b) == a


a = int(input("Nhập giá trị của a:"))
b = int(input("Nhập giá trị của b:"))
if is_amicable(a, b):
    print(f"{a} và {b} là số amicable.")
else:
    print(f"{a} và {b} không phải là số amicable.")
