def find_password(n):
    result = ""
    for d in range(1, n + 1):
        if n % d == 0:
            for i in range(1, d // 2 + 1):
                j = d - i
                if i + j == d:
                    result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
password = find_password(n)
print("Пароль:", password)