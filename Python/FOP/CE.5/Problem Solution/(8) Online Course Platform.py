class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email
    @property
    def username(self):
        return self.username
    @property
    def email(self):
        return self.email
class Instructor(User):
    def __init__(self, username, email):
        super().__init__(self._username,self._email)
        self._courses_taught = []
    def assigned_courses(self, course):
        self._courses_taught.append(course)
class Student(User):
    def __init__(self, enrolled):
        super().__init__(self._username,self._email)
        self._enrolled_courses = []
    def enrolled(self,course):
        return self._enrolled_courses.append(course)
class Course:
    def __init__(self, title, instructor):
        self._title = title
        self._instructor = instructor
        self._students = []
        instructor.assigned_courses(self)
    def add_student(self, student):
        self._students.append(student)
        student.enroll(self)
    def __str__(self):
        student_str = ', '.join(s._username for s in self._students) or 'No students'
        return f'Course: {self._title}\nInstructor: {self._instructor._username}\nStudents: {student_str}'
