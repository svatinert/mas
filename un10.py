def sort_array_by_parity(nums):
    # Використовуємо два вказівника: left для парних і right для непарних чисел
    left, right = 0, len(nums) - 1
    
    while left < right:
        # Знаходимо перше непарне число зліва
        while left < len(nums) and nums[left] % 2 == 0:
            left += 1
        
        # Знаходимо перше парне число справа
        while right >= 0 and nums[right] % 2 != 0:
            right -= 1
        
        # Обмін значеннями парного і непарного чисел
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return nums

# Приклад використання
nums1 = [3, 1, 2, 4]
result1 = sort_array_by_parity(nums1)
print(result1)  # Виведе [2, 4, 3, 1]

nums2 = [0]
result2 = sort_array_by_parity(nums2)
print(result2)  # Виведе [0]