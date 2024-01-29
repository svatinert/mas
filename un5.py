def merge(nums1, m, nums2, n):
    # Індекс для nums1
    i = m - 1
    # Індекс для nums2
    j = n - 1
    # Індекс для об'єднаного масиву nums1
    k = m + n - 1

    # Починаємо з кінця і об'єднуємо nums1 і nums2 в порядку неспадання
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # Якщо елементи в nums2 ще залишились, їх потрібно додати в початок nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Приклад використання
nums1_1 = [1, 2, 3, 0, 0, 0]
m1 = 3
nums2_1 = [2, 5, 6]
n1 = 3
merge(nums1_1, m1, nums2_1, n1)
print(nums1_1)  # Виведе [1, 2, 2, 3, 5, 6]

nums1_2 = [1]
m2 = 1
nums2_2 = []
n2 = 0
merge(nums1_2, m2, nums2_2, n2)
print(nums1_2)  # Виведе [1]

nums1_3 = [0]
m3 = 0
nums2_3 = [1]
n3 = 1
merge(nums1_3, m3, nums2_3, n3)
print(nums1_3)  # Виведе [1]