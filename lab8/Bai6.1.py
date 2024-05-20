def is_odd(number):
    """Kiểm tra xem một số có phải là số lẻ hay không"""
    return number % 2 != 0

# Danh sách mẫu
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lọc các số lẻ trong danh sách
odd_numbers = list(filter(is_odd, numbers))

print("Các số lẻ trong danh sách là:", odd_numbers)
