def sum_num():
    i = 0
    while True:
        list = input('Введите числа через пробел или стоп символ для остановки(стоп символ Q: - ').split()
        for num in list:
            if num.upper() == 'Q':
                return i

            else:
                try:
                    i += int(num)
                except ValueError:
                    print(input('Чтобы выйти из программы введите Q'))
        print(f'Суммма чисел = {i}')


print(sum_num())

