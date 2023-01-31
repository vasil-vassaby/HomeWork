def input_class():
    return input('Какой класс? ').upper().strip()


def input_subject():
    return input('Какой предмет? ').lower()


def who_answer():
    return input('Кто будет отвечать у доски? ').title()


def what_mark():
    return input('На какую оценку ответил ученик? ')


def list_kids(journal: dict):
    for number, kid in enumerate(journal, 1):
        print(f'{number}. {kid:15} {journal.get(kid)}')


def lesson_over():
    print('Урок окончен! Все оценки выставлены в журнал.')
