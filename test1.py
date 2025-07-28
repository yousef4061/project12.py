class Student:
    def __init__(self, name, student_id, courses=[]):
        self.name = name
        self.student_id = student_id
        self.courses = courses.copy()
        self.teacher = None

    def study(self):
        if self.curses:
            courses_str = ", ".join(self.courses) for course in self.courses)
            print(f"{self.name} is studying the following courses: {courses_str}.")
        else:
            print(f"{self.name} has no courses to study.")

    def exam(self):
        if self.courses:
            courses_str = ", ".join(self.courses) for course in self.courses)
            print(f"{self.name} is taking exams for the following courses: {courses_str}.")
        else:
            print(f"{self.name} has no courses to take exams for.")    

    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"The course {course_name} has been removed for {self.name}.")
        else:
            print(f"The course {course_name} was not found for {self.name}.")

    @staticmethod
    def set_teacher(teacher_name):
        print(f"Teacher {teacher_name} has been set for all students.")

if __name__ == "__main__":
    student1 = Student("Ali Mohammadi", "12345", ["Math", "Physics"])
    student1.study()
    student1.exam()
    student1.remove_course("Math")
    student1.study()
    student2 = Student("Sara Ahmadi", "67890")
    student2.study()
    Student.set_teacher("Dr. Hosseini")
