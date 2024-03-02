class Student:
    '''Хранит всю информацию о студенте. Оценивает лекторов (rate_hw).
    Выводит данные о студенте. Сравнивает средние оценки студентов'''

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_score(self)}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return average_score(self) < average_score(other)


class Mentor:
    '''Родительский класс. Хранит информаию о менторах, лекторах и ревьюверах:
    имя, фамилия, список закреплённых курсов'''

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    '''Ссылается на класс Mentor. Выводит информацию о лекторе и сравнивает средние оценки за курсы.
        Оценки хранятся в self.grades'''

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_score(self)}'

    def __lt__(self, other):
        return average_score(self) < average_score(other)


class Reviewer(Mentor):
    '''Ссылается на родительский класс Mentor. Оценивает студентов (rate_hw).
       Выводит информацию о ревьювере.'''

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_score(person):
    '''Считает среднюю оценку'''

    for i in person.grades.values():
        return round(sum(i) / len(i), 2)


best_student_1 = Student('Harry', 'Potter', 'male')
best_student_1.courses_in_progress += ['Potions', 'Astronomy', 'Flying', 'DefenceAgainsttheDarkArts']
best_student_1.finished_courses += ['Dursley']

best_student_2 = Student('Naville', 'Longbottom', 'male')
best_student_2.courses_in_progress += ['Astronomy', 'Herbology', 'Flying', 'DefenceAgainsttheDarkArts']
best_student_2.finished_courses += ['Grandmother']

best_student_3 = Student('Ron', 'Weasley', 'male')
best_student_3.courses_in_progress += ['Astronomy', 'Flying', 'Potions', 'DefenceAgainsttheDarkArts']
best_student_3.finished_courses += ['BigFamily']

cool_mentor_1 = Mentor('Albus', 'Dumbledore')
cool_mentor_1.courses_attached += ['Hogwarts']

just_reviewer = Reviewer('Dementor', 'Sweet')

some_lecturer_1 = Lecturer('Severus', 'Snape')
some_lecturer_1.courses_attached += ['Potions', 'Flying', 'Herbology']

some_lecturer_2 = Lecturer('Minerva', 'MacGonagal')
some_lecturer_2.courses_attached += ['Astronomy', 'Flying']

some_lecturer_3 = Lecturer('Rimus', 'Lpin')
some_lecturer_3.courses_attached += ['Astronomy', 'Flying', 'DefenceAgainsttheDarkArts']

best_student_1.rate_hw(some_lecturer_1, 'Potions', 10)
best_student_1.rate_hw(some_lecturer_2, 'Astronomy', 2)
best_student_1.rate_hw(some_lecturer_3, 'DefenceAgainsttheDarkArts', 10)

just_reviewer.rate_hw(best_student_1, 'Flying', 10)
just_reviewer.rate_hw(best_student_2, 'Flying', 2)
just_reviewer.rate_hw(best_student_3, 'Flying', 8)

just_reviewer.rate_hw(best_student_1, 'DefenceAgainsttheDarkArts', 9)
just_reviewer.rate_hw(best_student_2, 'DefenceAgainsttheDarkArts', 8)
just_reviewer.rate_hw(best_student_3, 'DefenceAgainsttheDarkArts', 10)

print(best_student_1)


def student_average_score(student_list, course_name):
    '''Средняя оценка всех студентов по конкретному курсу'''

    for student in student_list:
        return round((sum(student.grades.get(course_name))) / len(student_list), 2)


def lecturer_average_score(lector_list, course_name):
    '''Средняя оценка всех лекторов по конкретному курсу'''

    for lector in lector_list:
        return round((sum(lector.grades.get(course_name))) / len(lector_list), 2)


st_list = [best_student_1, best_student_2, best_student_3]
lec_list = [some_lecturer_1, some_lecturer_2, some_lecturer_3]
