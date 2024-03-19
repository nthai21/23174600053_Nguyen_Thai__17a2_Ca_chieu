# Số năm
years_5 = 5
years_10 = 10

# Tính số tiền sau 5 năm
amount_after_5_years = 10000 * (1 + 0.06) ** years_5

# Tính số tiền sau 10 năm
amount_after_10_years = 10000* (1 + 0.06) ** years_10

# Tính tỷ lệ tăng trưởng
growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years * 100

# In kết quả
print("Số tiền sau 5 năm là:", round(amount_after_5_years, 2))
print("Số tiền sau 10 năm là:", round(amount_after_10_years, 2))
print("Tỷ lệ tăng trưởng sau 10 năm so với sau 5 năm là:", round(growth_rate, 2), "%")