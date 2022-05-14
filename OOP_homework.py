class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and (0 < grade < 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка при внесении данных о курсе или оценке Лекции')
            return 'Ошибка'

    def calculate_avg_grade(self):
        list_ = []
        for i, grades_list in self.grades.items():
            list_.extend(grades_list)
        if list_:
            avg_grade = sum(list_) / len(list_)
            return avg_grade
        return 0

    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} "
                f"\nСредняя оценка за лекции: {self.calculate_avg_grade()} "
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return 'Ошибка'
        if other.calculate_avg_grade() < self.calculate_avg_grade():
            print(f"Средний балл выше у студента: {self.name}")
        else:
            print(f"Средний балл выше у студента: {other.name}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_avg_grade(self):
        return Student.calculate_avg_grade(self)

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return 'Ошибка'
        if other.calculate_avg_grade() < self.calculate_avg_grade():
            print(f"Средний балл выше у лектора: {self.name}")
        else:
            print(f"Средний балл выше у лектора: {other.name}")

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.calculate_avg_grade()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка при внесении данных о курсе или оценке ДЗ')
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


# Students
first_student = Student('First', 'Student1', 'female')
first_student.courses_in_progress += ['Python', 'Java']
first_student.finished_courses += ['JS']

second_student = Student('Second', 'Student2', 'male')
second_student.courses_in_progress += ['Python', 'Java']
second_student.finished_courses += ['matlab']

student_list = [first_student, second_student]
# Lecturers
first_lecturer = Lecturer('First', 'Lecturer1')
first_lecturer.courses_attached += ['Python', 'Java']
second_lecturer = Lecturer('Second', 'Lecturer2')
second_lecturer.courses_attached += ['Python', 'Java']

lectures_list = [first_lecturer, second_lecturer]

# Reviewers
first_reviewer = Reviewer('First', 'Reviewer1')
first_reviewer.courses_attached += ['Python', 'Java']
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 20)

second_reviewer = Reviewer('Second', 'Reviewer2')
second_reviewer.courses_attached += ['Python', 'Java']
second_reviewer.rate_hw(second_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Python', 10)

first_student.rate_lecture(first_lecturer, 'Python', 1)
second_student.rate_lecture(second_lecturer, 'Java', 2)
second_student.rate_lecture(second_lecturer, 'Python', 5)

print(first_student)
print("-------------------------------------------------------")
print(second_student)
print("-------------------------------------------------------")
print(first_lecturer)
print("-------------------------------------------------------")
print(second_lecturer)
print("-------------------------------------------------------")
print(first_reviewer)
print("-------------------------------------------------------")
print(second_reviewer)
print("-------------------------------------------------------")

first_lecturer.__lt__(second_lecturer)
first_student.__lt__(second_student)


def avg_grade_students(list_of_students, course_name):
    list_ = []
    avg_grade = 0
    for student in list_of_students:
        for course, grades_list in student.grades.items():
            if course == course_name:
                list_.extend(grades_list)
            if list_:
                avg_grade = sum(list_) / len(list_)
    print(f'Средняя оценка студентов за курс {course_name} составляет: {round(avg_grade, 1)}')


def avg_grade_lectors(list_of_lectures, course_name):
    list_ = []
    avg_grade = 0
    for lecture in list_of_lectures:
        for course, grades_list in lecture.grades.items():
            if course == course_name:
                list_.extend(grades_list)
            if list_:
                avg_grade = sum(list_) / len(list_)
    print(f'Средняя оценка лекторов за курс {course_name} составляет: {round(avg_grade, 1)}')


avg_grade_students(student_list, 'Python')
avg_grade_lectors(lectures_list, 'Python')
