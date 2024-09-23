def find_password(n):
    result = ""
    for i in range(1, n // 2 + 1):
        sum_nbr = i + (n - i)
        if n % sum_nbr == 0:
            result += str(i) + str(n - i)
    return result


n = int(input("Введите число от 3 до 20: "))
password = find_password(n)
print("Пароль:", password)
