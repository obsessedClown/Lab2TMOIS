def unification(first_set: list, second_set: list):  # создание функции для объединения множеств
    c = []  # создание пустого списка
    for x in range(len(first_set)):  # добавление элементов списка А и В в список С
        c.append(first_set[x])
    for y in range(len(second_set)):
        if second_set[y] not in c:
            c.append(second_set[y])
    print("Результат выполнения операции объединения: \n", c)


def intersection(first_set: list, second_set: list):  # создание функции для объединения множеств
    c = []  # создание пустого списка
    for x in range(len(first_set)):
        for y in range(len(second_set)):
            if first_set[x] == second_set[y]:  # сравнивание элементов списка А с элементами списка В
                c.append(first_set[x])  # добавление эквивалентных элементов из списка А и В в список С
    print("Результат выполнения операции пересечения: \n", c)


def difference(first_set: list, second_set: list):
    c = []
    for x in range(len(first_set)):
        if first_set[x] not in second_set:
            c.append(first_set[x])
    print("Результат выполнения операции разности: \n", c)


def symmetric_difference(first_set: list, second_set: list):
    c = []
    for x in range(len(first_set)):
        if first_set[x] not in second_set:
            c.append(first_set[x])
    for y in range(len(second_set)):
        if second_set[y] not in first_set:
            c.append(second_set[y])
    print("Результат выполнения операции симметрической разности: \n", c)


def addition(first_set: list, uni_set: list):
    c = []
    for y in range(len(uni_set)):
        if uni_set[y] not in first_set:
            c.append(uni_set[y])
    print("Результат выполнения операции дополнение: \n", c)


def cartesian_product(first_set: list, second_set: list):
    c = []
    for x in range(len(first_set)):
        for y in range(len(second_set)):
            c.append([first_set[x], second_set[y]])
    print(c)


lenA = int(input("Введите мощность множества A: "))
lenB = int(input("Введите мощность множества B: "))  # ввод мощностей множеств А и В

if lenA > 20 or lenB > 20:  # вводим условие того, что вводимая пользователем мощность множеств А и В не должна
    # превышать 20
    print("Мощность множества не должна превышать 20! ")  # выводим на экран сообщений об ошибке
    quit()  # выходим из программы в связи с ошибкой

A, B = [], []  # создаем пустые списки А и В
print("Введите элементы мноества А: ")
for iA in range(lenA):  # ввод элементов списка А
    a = int(input())
    if a > 50:  # вводим условие того, что значение вводимых элементов не должно превышать 50
        print("Элементы множества не должны превышать 50! ")  # выводим на экран сообщений об ошибке
        quit()  # выходим из программы в связи с ошибкой
    elif a not in A:
        A.append(a)  # добавление элементов в список А
    else:
        print("Во множестве не может быть одинаковых элементов!")
        quit()

print("Введите элементы мноества В: ")
for iB in range(lenB):  # ввод элементов списка B
    b = int(input())
    if b > 50:  # вводим условие того, что значение вводимых элементов не должно превышать 50
        print("Элементы множества не должны превышать 50! ")  # выводим на экран сообщений об ошибке
        quit()  # выходим из программы в связи с ошибкой
    elif b not in B:
        B.append(b)  # добавление элементов в список А
    else:
        print("Во множестве не может быть одинаковых элементов!")
        quit()

universe = []
for a in range(1, 51, 1):
    universe.append(a)

operation_selection = int(input("Выберите операцию: 1 - объединение; 2 - пересечение; 3 - разность; 4 - симметрическая "
                                "разность; 5 - дополнение до универсума; 6 - декартово произведение; \n"))

match operation_selection:
    case 1:
        unification(A, B)
    case 2:
        intersection(A, B)
    case 3:
        difference_selection = int(input("Выберите порядок следования множеств: 1 - A и B; 2 - B и A; \n"))
        match difference_selection:
            case 1:
                difference(A, B)
            case 2:
                difference(B, A)
    case 4:
        symmetric_difference(A, B)
    case 5:
        addition_selection = int(input("Выберите, для какого множества выполнить операцию дополнения: 1 - для "
                                       "множества A; 2 - для множества B; \n"))
        match addition_selection:
            case 1:
                addition(A, universe)
            case 2:
                addition(B, universe)
    case 6:
        cartesian_product_selection = int(input("Выберите порядок следования множеств: 1 - A и B; 2 - B и A; \n"))
        match cartesian_product_selection:
            case 1:
                cartesian_product(A, B)
            case 2:
                cartesian_product(B, A)