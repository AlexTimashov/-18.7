import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценку ученика по предмету
        2. Удаление оценки ученика по предмету
        3. Редактирование оценки ученика по предмету
        4. Добавление ученика
        5. Добавление предмета
        6. Вывести средний балл по всем предметам по каждому ученику
        7. Вывести все оценки по всем ученикам
        8. Вывести информацию по всем оценкам для определенного ученика
        9. Вывести средний балл по каждому предмету по определенному ученику
        10. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку от 1 до 5: '))
        # Нет проверки по введенным оценкам
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Удаление оценки ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(students_marks[student][class_])
            marks = students_marks[student][class_]
            # считываем оценку, которую нужно удалить
            index = int(input(f'Введите индекс оценки, которую нужно удалить от 0 до {len(marks) - 1}: '))
            del_mark = marks.pop(index)
            print(f'Удаленная оценка: {del_mark}')
            print(f'Список оценок для {student} по предмету {class_}: {students_marks[student][class_]}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 3:
        print('3. Редактирование оценки ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(students_marks[student][class_])
            marks = students_marks[student][class_]
            # считываем оценку, которую нужно удалить
            index = int(input(f'Введите индекс оценки, которую нужно отредактировать от 0 до {len(marks) - 1}: '))
            mark = int(input('Введите оценку от 1 до 5: '))
            # Нет проверки по введенным оценкам
            students_marks[student][class_][index] = mark
            print(f'Список оценок для {student} по предмету {class_}: {students_marks[student][class_]}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 4:
        print('4. Добавление ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        students.append(student)
        print(f'Список всех учеников: {students}')
    elif command == 5:
        print('5. Добавление предмета')
        # считываем название предмета
        class_ = input('Введите название предмета: ')
        classes.append(class_)
        print(f'Список всех предметов: {classes}')
    elif command == 6:
        print('6. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'\t{class_} - {marks_sum // marks_count}')
            print()
    elif command == 7:
        print('7. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 8:
        print('8. Вывести информацию по всем оценкам для определенного ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # Проверяем, есть ли такой ученик
        if student in students:
            # print(students_marks[student]) - не понравилось отображение в строку!!!
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 9:
        print('9. Вывести средний балл по каждому предмету по определенному ученику')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # Проверяем, есть ли такой ученик
        if student in students:
            # Вывод среднего балла по каждому предмету по ученику
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'\t{class_} - {marks_sum // marks_count}')
        # неверно введено имя ученика
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 10:
        print('10. Выход из программы')
        break
