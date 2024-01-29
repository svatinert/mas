def max_ones_count(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Приклад використання
nums1 = [1, 1, 0, 1, 1, 1]
print(max_ones_count(nums1))  # Виведе 3

nums2 = [1, 0, 1, 1, 0, 1]
print(max_ones_count(nums2))  # Виведе 2