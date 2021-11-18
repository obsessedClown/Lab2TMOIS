def unifi(a: list, b: list):  # создание функции для объединения множеств
    c = []  # создание пустого списка
    for x in range(len(a)):  # добавление элементов списка А и В в список С
        c.append(a[x])
    for y in range(len(b)):
        if b[y] not in c:
            c.append(b[y])
    print("Результат выполнения операции объединения: \n", c)


def inters(a: list, b: list):  # создание функции для объединения множеств
    c = []  # создание пустого списка
    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y]:  # сравнивание элементов списка А с элементами списка В
                c.append(a[x])  # добавление эквивалентных элементов из списка А и В в список С
    print("Результат выполнения операции пересечения: \n", c)


def diff(a: list, b:list):
    c = []
    for x in range(len(a)):
        if a[x] not in b:
            c.append(a[x])
    print("Результат выполнения операции разности: \n", c)


def diff1_2(a: list, b:list):
    c = []
    for x in range(len(a)):
        if a[x] not in b:
            c.append(a[x])
    print("Результат выполнения операции разности: \n", c)


def diff2_1(a: list, b:list):
    c = []
    for y in range(len(b)):
        if b[y] not in a:
            c.append(b[y])
    print("Результат выполнения операции разности: \n", c)


def symm_diff(a: list, b:list):
    c = []
    for x in range(len(a)):
        if a[x] not in b:
            c.append(a[x])
    for y in range(len(b)):
        if b[y] not in a:
            c.append(b[y])
    print("Результат выполнения операции симметрической разности: \n", c)


def addition(a: list, b:list):
    c = []
    for y in range(len(b)):
        if b[y] not in a:
            c.append(b[y])
    print("Результат выполнения операции дополнение: \n", c)


lenA = int(input("Введите мощность множества A: "))
lenB = int(input("Введите мощность множества B: "))  # ввод мощностей множеств А и В

if lenA > 20 or lenB > 20:  # вводим условие того, что вводимая пользователем мощность множеств А и В не должна превышать 20
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

universum = []
for a in range(1,51,1):
    universum.append(a)

choise = int(input("Выберите операцию: 1 - объединение; 2 - пересечение; 3 - разность(1-2); 4 - разность(2-1); "
                   "5 - симметрическая разность; 6 - дополнение(A); 7 - дополнение(B); \n"))

match choise:
    case 1:
        unifi(A, B)
    case 2:
        inters(A, B)
    case 3:
        diff(A, B)
    case 4:
        diff(B, A)
    case 5:
        symm_diff(A, B)
    case 6:
        addition(A, universum)
    case 7:
        addition(B, universum)
