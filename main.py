class AverageGradeMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grades = {}
    def average_grade(self):
        if not self.grades:
            return "N/a"
        total_grade = 0
        grade_count = 0
        for course, grade_list in self.grades.items():
            grade_count += len(grade_list)
            total_grade += sum(grade_list)
        return total_grade / grade_count


class Student(AverageGradeMixin):
    def __init__(self, name, surname, gender):
        super().__init__()
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(AverageGradeMixin, Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(best_student.average_grade())

lekter = Lecturer("Hannibal", "Lekter")
lekter.courses_attached += ['Python']
best_student.rate_lecture(lekter, 'Python', 10)
best_student.rate_lecture(lekter, 'Python', 9)
best_student.rate_lecture(lekter, 'Python', 8)
print(lekter)
print(best_student)