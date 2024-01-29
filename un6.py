def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # Індекс для унікальних елементів

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

# Приклад використання
nums1 = [1, 1, 2]
result1 = remove_duplicates(nums1)
print(result1, nums1[:result1])  # Виведе 2 [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = remove_duplicates(nums2)
print(result2, nums2[:result2])  # Виведе 5 [0, 1, 2, 3, 4]
