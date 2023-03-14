# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

students_dict = {}
for student in students:
    name_student = student['first_name']
    if name_student in students_dict:
        students_dict[name_student] += 1
    else:
        students_dict[name_student] = 1

for stud in students_dict:
    print(f'{stud}: {students_dict[stud]}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

students_dict = {}
for student in students:
    name_student = student['first_name']
    if students_dict.get(name_student) != None:
        students_dict[name_student] += 1
    else:
        students_dict[name_student] = 1
       
print(f'Самое частое имя среди учеников: {max(students_dict, key=students_dict.get)}')



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for count,school_stud in enumerate(school_students, start=1):
    students_dict = {}
    for student in school_stud:
        name_student = student['first_name']
        if students_dict.get(name_student) != None:
            students_dict[name_student] += 1
        else:
            students_dict[name_student] = 1
       
    print(f'Самое частое имя в классе {count}: {max(students_dict, key=students_dict.get)}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for group in school:
    number_group = group['class']
    students = group['students']
    students_girls = 0
    students_boys = 0
    for student in students:
        name_student = student['first_name']
        gender = is_male[name_student]
        if not gender:
            students_girls += 1       
        else:
            students_boys += 1
        
    print(f'Класс {number_group}: девочки {students_girls}, мальчики {students_boys}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# создать два словаря ключи - номера классов
# 

boys_dict = {}
girls_dict = {}
for group in school:
    number_group = group['class']
    students = group['students']
    students_girls = 0
    students_boys = 0
    for student in students:
        name_student = student['first_name']
        gender = is_male[name_student]
        if not gender:
            students_girls += 1       
        else:
            students_boys += 1
    boys_dict[number_group] = students_boys
    girls_dict[number_group] = students_girls

print(f'Больше всего мальчиков в классе {max(boys_dict, key=boys_dict.get)}')
print(f'Больше всего девочек в классе {max(girls_dict, key=girls_dict.get)}')

# вообще-то по итогу последнего принта я думала, что выведется 'Больше всего мальчиков в классе 3c 2', почему вывод без числа так и не поняла) но итог верный, ура
