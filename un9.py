def replace_elements(arr):
    n = len(arr)
    
    if n == 1:
        return [-1]

    max_right = -1
    for i in range(n - 1, -1, -1):
        current_element = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current_element)

    return arr

# Приклад використання
arr1 = [17, 18, 5, 4, 6, 1]
result1 = replace_elements(arr1)
print(result1)  # Виведе [18, 6, 6, 6, 1, -1]

arr2 = [400]
result2 = replace_elements(arr2)
print(result2)  # Виведе [-1]