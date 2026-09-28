class Student:
    def __init__(self, student_id, name):
        self._id = student_id
        self._name = name

    @property
    def student_id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Student {self._id}: {self._name}"


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

    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)
            return True
        return False  # already enrolled

    def __str__(self):
        students_str = ", ".join(str(s) for s in self._students) or "No students"
        return f"Course {self._code}: {self._title}\n  Students: {students_str}"


class University:
    def __init__(self):
        self._courses = []
        self._students = []

    def add_student(self, student):
        # Check for duplicate student ID
        for s in self._students:
            if s.student_id == student.student_id:
                print(f"Error: Student with ID {student.student_id} already exists.")
                return False
        self._students.append(student)
        return True

    def add_course(self, course):
        # Check for duplicate course code
        for c in self._courses:
            if c.code == course.code:
                print(f"Error: Course with code {course.code} already exists.")
                return False
        self._courses.append(course)
        return True

    def enroll_student(self, course_code, student):
        # Step 1: Check if student exists
        if student not in self._students:
            print(f"Error: Student {student.name} is not registered at the university.")
            return False

        # Step 2: Find the course
        for course in self._courses:
            if course.code == course_code:
                success = course.add_student(student)
                if not success:
                    print(f"Error: Student {student.name} is already enrolled in {course_code}.")
                return success

        # Step 3: If no course found
        print(f"Error: Course '{course_code}' not found in university.")
        return False

    def __str__(self):
        courses_str = "\n".join(str(c) for c in self._courses) or "No courses"
        return f"University Courses:\n{courses_str}"


# -------------------------------
# Example usage
# -------------------------------

uni = University()

# Create and add courses
c1 = Course("CS101", "Intro to Programming")
c2 = Course("MATH201", "Calculus")
uni.add_course(c1)
uni.add_course(c2)

# Create and add students
s1 = Student(1, "Alice")
s2 = Student(2, "Bob")
s3 = Student(3, "Eve")
uni.add_student(s1)
uni.add_student(s2)

# Enroll students
uni.enroll_student("CS101", s1)
uni.enroll_student("CS101", s2)
uni.enroll_student("MATH201", s1)

# Try invalid enrollments
uni.enroll_student("HIST300", s1)  # course doesn’t exist
uni.enroll_student("CS101", s3)    # student not registered
uni.enroll_student("CS101", s1)    # duplicate enrollment

# Print final university state
print("\n" + "="*40)
print(uni)

            
    
    
    
            
        