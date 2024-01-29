def duplicate_zeros(arr):
    i = 0
    length = len(arr)

    while i < length:
        if arr[i] == 0:
            # Вставляємо 0 і зсуваємо решту елементів вправо
            arr.insert(i, 0)
            arr.pop()
            i += 2  # Переходимо через новий вставлений 0
        else:
            i += 1

# Приклад використання
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)  # Виведе [1, 0, 0, 2, 3, 0, 0, 4]

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2)  # Виведе [1, 2, 3]