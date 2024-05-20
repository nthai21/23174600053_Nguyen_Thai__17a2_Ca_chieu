def is_prime(n):
    """Kiểm tra xem n có phải là số nguyên tố hay không"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True

def print_twin_primes(limit):
    """In các số nguyên tố sinh đôi nhỏ hơn limit"""
    prev_prime = 2  # Số nguyên tố trước đó
    for num in range(3, limit, 2):
        if is_prime(num):
            if num - prev_prime == 2:
                print(prev_prime, num)
            prev_prime = num
print_twin_primes(1000)
