# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
def encode(s):
    encoding = ""  # сохраняет выходную строку

    i = 0
    while i < len(str(s)):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(str(s)) and str(s)[i] == str(s)[i + 1]:
            count = count + 1
            i = i + 1

        # добавляет к результату текущий символ и его количество
        encoding += str(count) + str(s)[i]
        i = i + 1

    return encoding

alp = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
digits = 111112222334445

print(encode(digits))



