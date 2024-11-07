# однострочный комментарий
# integer (int) - целые числа
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

c = a + b
d = a * b

print(c)
print(d)

#Float (float) - вещественные числа
float_a = 0.5
float_b = 1.25

print(type(a))
print(type(float_a))

# Boolean - логический тип данных

is_active = True
is_logout = False


print(is_active or is_logout)
print(is_active and is_logout)
print((not is_active) and is_logout)

print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)

#сколько места в памяти содержит переменная

print(id(a))

# приведение строки к типу (int)
age = "15"
year = "2024"

print(int(age)+ int(year))

# string (str) -  строковый тип данных. Строки в пайтоне неизменяемые!

text = "I 'love' Python"
print(text)

# None -

flag = None

#СТРУКТУРЫ ДАННЫХ

# list () - [] -  спсики

cars = ['bmw','ford','audi',24,True,[1,2]]

# dict () - {} - словари

info = {
    'name': 'Kora',
    'cars': cars,
}

# tuple - () - Кортежи.   Список который нельзя изменить! Нельзя добавить или удалить элементы и нельзя удалить сам список

colors = (
    ('red','255,0,0'),
    ('blue', '0,0,255')
)

# set - set() - множества - {}. Множества удаляют все повторяющиеся эелементы

set_numbers = {1,2,3,4,5,6,6,6,6}
print(set_numbers)

# функции
# файлы
# классы


# регистро-зависимый язык. больша и маленькая буквы-разные переменные
name = 5
Name = 5

#многострочный комментарий """ fgjgkjfhgkjf """, '''dfhjdjfdkjhfjdkhf'''
"""jfdhgfjhgjf
dgjhdkjsgg
gfjgkghkjf"""

'''fhjdkjfhdkfdkl
fdskjbfdkjsbf
dsfbdkjbfdkjbf'''

number = 6
print(number)

#  ввод данных из консоли
name = input("Введите свое имя: ")
age = input("Сколько вам лет? ")
print("Hello", name)
print("Вам", age, "года")



