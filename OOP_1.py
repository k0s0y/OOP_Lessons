# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#
#
# peter = Character()
# peter.name = 'Peter Parker'
# peter.power = 70
# peter.alias = 'Spider-man'
#
# bruce = Character()
# bruce.name = 'Bruce Wane'
# bruce.power = 90
# bruce.alias = 'Batman'


# print(Character.__dict__)
# print(dir(Character))
# print(peter.__dict__)
# print(bruce.__dict__)


# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#     backpack = []
#
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
#
#     def train(self, hours):
#         if self.energy >= 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
#
#     def change_alias(self, new_alias):
#         # print(self)
#         self.alias = new_alias
#
#
# bruce = Character()
# peter = Character()
# peter.backpack.append('shotgun')


# class Character:
#     name = ''
#     power = 0
#     energy = 100
#     hands = 2
#
#
# peter = Character()
# peter.name = 'Peter Parker'
# peter.power = 70
# peter.alias = 'Spider-man'
#
# bruce = Character()
# bruce.name = 'Bruce Wane'
# bruce.power = 90
# bruce.alias = 'Batman'


# print(Character.__dict__)
# print(dir(Character))
# print(peter.__dict__)
# print(bruce.__dict__)


class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.backpack = []
        self.hands = hands

    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def train(self, hours):
        if self.energy >= 0:
            self.energy -= hours * 2
            self.power += hours * 2
        else:
            print('Too tired')

    def change_alias(self, new_alias):
        # print(self)
        self.alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Character):
            return
        if foe.power < self.power:
            foe.status = 'defeated'
            self.status = 'winner'
        else:
            print('Retreat!')


bruce = Character('Bruce Wane', 100)
peter = Character('Peter Parker', 80)
peter.backpack.append('shotgun')
print(peter.backpack)
print(bruce.backpack)

bruce.beat_up(peter)
print(bruce.status)


# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#         def add_courses(self, course_name):
#             self.finished_course.append(course_name)
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)


13.8