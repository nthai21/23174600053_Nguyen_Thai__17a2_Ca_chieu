def sumPdivisors(n):
    """Tính tổng các ước số chính của số nguyên n, ngoại trừ chính số đó"""
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

number=int(input("Mời nhập giá trị"))
print(f"Tổng các ước số chính của {number} là: {sumPdivisors(number)}")
