# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data(**kwargs):
    return' '.join(kwargs.values())

print((data(name=input('Введите имя - '), second=input('Введите фамилию - '),birthday=input('Введите ваш день рождения - ') , city=input('Введите ваш город - '), mail=input('Введите вашу электронную почту - '), phoneNumber=input('Введите ваш номер телефона - ', ))))


#def data_f(name, second, birthday, city, mail, phoneNumber):
   # return f'Имя - {name}; Фамилия - {second}; День рождения - {birthday}"'\
    #      f'Город - {city}; Электронная почта - {mail}; Номер телефона - {phoneNumber}'
#print(data_f(name="Вера", second="Вилкова", birthday="10.11.1980" , city="Санкт-Петербург", mail="VilkV@gmailcom", phoneNumber="8-915-66-556"))

