def sorted_squares(nums):
    # Квадрати кожного числа
    squares = [num ** 2 for num in nums]

    # Сортування квадратів за неспаданням
    squares.sort()

    return squares

# Приклад використання
nums1 = [-4, -1, 0, 3, 10]
result1 = sorted_squares(nums1)
print(result1)  # Виведе [0, 1, 9, 16, 100]

nums2 = [-7, -3, 2, 3, 11]
result2 = sorted_squares(nums2)
print(result2)  # Виведе [4, 9, 9, 49, 121]