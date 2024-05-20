def is_even(number):
    """Kiểm tra xem một số có phải là số chẵn hay không"""
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = list(filter(is_even, numbers))

print("Các số chẵn trong danh sách là:", even_numbers)
