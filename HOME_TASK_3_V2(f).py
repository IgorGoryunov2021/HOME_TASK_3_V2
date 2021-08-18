#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#но с прописной первой буквой.
#Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов,
#разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
#Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
#Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
     lwords = 'abcdefghijklmnopqrstuvyxyz'
     return word.title() if not set(word).difference(lwords) else False


words = input('Введите буквы латинского алфавита в нижнем регистре').split()
for w in words:
     result = int_func(w)
     if result:
        print(int_func(w), '')

# def int_func():
#     for word in input('enter words :\n').split():
#         chars = 0
#         for char in word:
#             if 97 <= ord(char) <= 122:
#                 chars += 1
#         print(word.title() if chars == len(word) else f'{word} - только маленькие буквы')
#
#
# print(int_func()) -----Разбирал ваш пример.





#w_m_func(w_1=(input('Введите латинские буквы разделенные пробелом'))
