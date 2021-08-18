def m_n_f(x,y):
    try:
        result = (x ** y)
    except TypeError:
        return ' Ошибка: Введите целое число'
    return result

print(float(m_n_f(x=20,y=-2)))


