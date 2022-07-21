from numpy import mean


class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_exam(self, _grade: float):
        self.grades.append(_grade)

    def get_mean(self):
        return mean(self.grades)


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, _student: Student):
        self.students.append(_student)

    def get_mean(self):
        return sum(x.get_mean() for x in self.students) / len(self.students)

    def get_best_student(self):
        largest_student_mean = 0
        best_student = self.students[0]
        for stu in self.students:
            if stu.get_mean() > largest_student_mean:
                best_student = stu
        return best_student


class City:
    def __init__(self, name):
        self.name = name
        self.schools = []

    def add_school(self, _school: School):
        self.schools.append(_school)

    def get_mean(self):
        return sum(x.get_mean() for x in self.schools) / len(self.schools)

    def get_best_school(self):
        largest_school_mean = 0
        best_school = self.schools[0]
        for school in self.schools:
            if school.get_mean() > largest_school_mean:
                largest_school_mean = school.get_mean()
                best_school = school
        return best_school

    def get_best_student(self):
        largest_student_mean = 0
        best_student = self.schools[0].students[0]
        for sch in self.schools:
            for stu in sch.students:
                if stu.get_mean() > largest_student_mean:
                    best_student = stu
        return best_student


if __name__ == "__main__":
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_grades in (('alice', (1, 2, 3)),
                                         ('bob', (2, 3, 4)),
                                         ('catherine', (3, 4, 5)),
                                         ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for grade in student_grades:
            student.add_exam(grade)
        hkis.add_student(student)

    print(hkis.get_best_student().name)
    print(paris.get_mean())
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)
