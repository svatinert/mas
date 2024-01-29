def valid_mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False
    
    peak_index = arr.index(max(arr))
    
    if peak_index == 0 or peak_index == n - 1:
        return False
    
    # Перевірка строгого зростання до піку
    for i in range(1, peak_index):
        if arr[i] <= arr[i - 1]:
            return False
    
    # Перевірка строгого спадання після піку
    for i in range(peak_index + 1, n):
        if arr[i] >= arr[i - 1]:
            return False
    
    return True

# Приклад використання
arr1 = [2, 1]
result1 = valid_mountain_array(arr1)
print(result1)  # Виведе False

arr2 = [3, 5, 5]
result2 = valid_mountain_array(arr2)
print(result2)  # Виведе False

arr3 = [0, 3, 2, 1]
result3 = valid_mountain_array(arr3)
print(result3)  # Виведе True