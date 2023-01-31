import model as md
import view as vw
import os


def start():
    while True:
        path = md.set_class(vw.input_class())
        if os.path.exists(path):
            while True:
                lesson = md.set_subject(vw.input_subject())
                md.open_file()
                lessons = md.get_lesson_list()
                if lesson in lessons:
                    while True:
                        journal = md.get_journal()
                        vw.list_kids(journal)
                        student = vw.who_answer()
                        if student in journal:
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
                        elif student == 'Выход':
                            vw.lesson_over()
                            break
                        else:
                            print(f'Ученика "{student}" нет в журнале! '
                                  'Введите полностью имя и фамилию школьника '
                                  'из предложенного ниже списка')
                    md.save_file()
                    break
                else:
                    print('Укажите полное название предмета из предложенного списка!')
                    print(lessons)
            break
        else:
            print('Укажите существующий класс!')
