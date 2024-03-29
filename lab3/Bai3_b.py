''' In ra các số chính phương từ 1 đến 1000 (kể cả số 1000)
Số Chính Phương (Perfect Square): Đây là các số nguyên dương mà có căn bậc
hai là một số nguyên dương. Nói cách khác, nếu một số là bình phương của
một số nguyên dương khác, thì số đó được gọi là số chính phương. Ví dụ: 1, 4,
9, 16, 25 là các số chính phương vì căn bậc hai của chúng là một số nguyên'''
print("---------------------------------Bài làm---------------------------------")
import math
print("Các số chính phương từ 1 đến 1000 là:")
for i in range(1, 1001):
    if int(i ** 0.5) ** 2 == i:
        print(i, end=" ,")
