def cubesum(n):
    n_str = str(n)
    
    total = sum(int(digit) ** 3 for digit in n_str)
    
    return total
result = cubesum(123)
print(result)  
