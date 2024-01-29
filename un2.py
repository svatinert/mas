def count_numbers_with_even_digits(nums):
    def count_digits(num):
        count = 0
        while num:
            count += 1
            num //= 10
        return count

    even_digits_count = 0
    for num in nums:
        if count_digits(num) % 2 == 0:
            even_digits_count += 1

    return even_digits_count

# Приклад використання
nums1 = [12, 345, 2, 6, 7896]
result1 = count_numbers_with_even_digits(nums1)
print(result1)  # Виведе 2

nums2 = [555, 901, 482, 1771]
result2 = count_numbers_with_even_digits(nums2)
print(result2)  # Виведе 1