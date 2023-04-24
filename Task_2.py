def minOperation(size, i, j):
    # Базовый случай: одна матрица
    if j - i <= 1:
        return 0

    # Минимальное значение
    minSize = 10 ** 20

    # Рассматриваем все случаи разделения матриц
    for k in range(i + 1, j):
        thisSize = minOperation(size, i, k) + minOperation(size, k, j) + size[i] * size[k] * size[j] # Рекурсивно подсчитываем thisSize
        minSize = min(minSize, thisSize) # Проверка на минимум

    return minSize # Вывод минимума


mySizeArray = [10, 30, 5, 60]
print(minOperation(mySizeArray, 0, len(mySizeArray) - 1))