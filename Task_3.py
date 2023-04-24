import random

n = int(input('Введите число элементов списка: '))
array = [random.randint(-100, 100) for _ in range(n)]
answer = demoAnswer = 1

for i in range(n - 1):
    if array[i + 1] > array[i]:
        demoAnswer += 1
    else:
        answer = max(answer, demoAnswer)
        demoAnswer = 1

print(array, answer)
