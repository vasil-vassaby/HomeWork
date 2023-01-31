
journal = {}
subject = ''
path = ''
lesson_list = []


def set_class(class_path: str):
    global path
    path = 'Classes/' + class_path + '.txt'
    return path


def set_subject(current_subj: str):
    global subject
    subject = current_subj
    return subject


def open_file():
    global journal
    global path
    global subject
    global lesson_list
    with open(path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(';')
        lesson_list.append(line[0])
        if line[0] == subject:
            students_list = line[1].split(',')
            for student in students_list:
                student = student.split(':')
                journal[student[0]] = list(map(int, student[1].split()))


def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as file:
        file = file.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ','.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(new_file))


def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks


def get_journal():
    return journal


def get_lesson_list():
    global lesson_list
    return lesson_list
