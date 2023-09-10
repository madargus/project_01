# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4
import sqlite3

conn = sqlite3.connect('teachers.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Students
                  (Student_Id INTEGER, Student_Name TEXT, School_Id INTEGER PRIMARY KEY)''')

students_data = [(201, 'Иван', 1),
                 (202, 'Петр', 2),
                 (203, 'Анастасия', 3),
                 (204, 'Игорь', 4)]

cursor.executemany('INSERT INTO Students VALUES (?,?,?)', students_data)

conn.commit()
conn.close()

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3

conn = sqlite3.connect('teachers.db')
cursor = conn.cursor()


def get_student_info(student_id):
    cursor.execute('''SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name
                      FROM Students
                      INNER JOIN School ON Students.School_Id = School.School_Id
                      WHERE Students.Student_Id = ?''', (student_id,))

    result = cursor.fetchone()

    if result:
        print('ID Студента:', result[0])
        print('Имя студента:', result[1])
        print('ID школы:', result[2])
        print('Название школы:', result[3])
    else:
        print('Студент с указанным ID не найден')


student_id = int(input("Для получения информации введите ID студента: "))
get_student_info(student_id)

conn.close()
