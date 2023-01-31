import model as md
import view as vw
import os


def start():
    while True:
        path = md.set_class(vw.input_class())
        if os.path.exists(path):
            check_subject()
            break
        else:
            print('Укажите существующий класс!')


def check_mark(student: str):
    while True:
        try:
            mark = int(vw.what_mark())
            if 0 < mark < 6:
                md.student_mark(student, mark)
                break
            else:
                print('Укажите оценку от 1 до 5!')
        except ValueError:
            print('Укажите целое число!')


def check_student():
    while True:
        journal = md.get_journal()
        vw.list_kids(journal)
        student = vw.who_answer()
        if student in journal:
            check_mark(student)
        elif student == 'Выход':
            vw.lesson_over()
            break
        else:
            print(f'Ученика "{student}" нет в журнале! '
                  'Введите полностью имя и фамилию школьника '
                  'из предложенного ниже списка')


def check_subject():
    while True:
        lesson = md.set_subject(vw.input_subject())
        md.open_file()
        lessons = md.get_lesson_list()
        if lesson in lessons:
            check_student()
            md.save_file()
            break
        else:
            print('Укажите полное название предмета из предложенного списка!')
            print(lessons)
