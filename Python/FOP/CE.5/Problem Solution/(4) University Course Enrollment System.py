class Student:
    def __init(self, st_id, name):
        self._id = st_id
        self._name = name
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    def __str__(self):
        return f"id: {self._id} \n name: {self._name}"
class Course:
    def __init__(self, code, title):
        self._code = code
        self._title = title
        self._students = []
    @property
    def code(self):
        return self._code
    @property
    def title(self):
        return self._title
    @property
    def students(self):
        return self._students
    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)
    def __str__(self):
        students_str = ', '.join(str(s) for s in self._students)
        return f" {self._code}: {self.title} \n Students: {students_str}"
class University:
    def __init__(self):
        self._courses = []
    def add_course(self, course):
        self._courses.append(course)
    def enroll_student(self, course_code, student):
        for course in self._courses:
            if course._code == course_code:
                course.add_student(student)
                return True
        return False
    def __str__(self):
        return f'\n'.join(str(c) for c in self._courses)
