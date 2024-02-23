from django.test import TestCase
from E_Learning_Platform.models import Student, Course, Assignment

class ModelTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.student = Student.objects.create(first_name='John', last_name='Doe', date_of_birth='2000-01-01', address='123 Main St')
        self.course = Course.objects.create(name='Mathematics', description='Introduction to Mathematics', instructor='Prof. Smith')
        self.assignment = Assignment.objects.create(course=self.course, title='Homework 1', description='Complete exercises 1-5', deadline='2024-02-28')

    def test_student_creation(self):
        # Test if the student was created successfully
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.last_name, 'Doe')
        self.assertEqual(self.student.date_of_birth, '2000-01-01')
        self.assertEqual(self.student.address, '123 Main St')

    def test_course_creation(self):
        # Test if the course was created successfully
        self.assertEqual(self.course.name, 'Mathematics')
        self.assertEqual(self.course.description, 'Introduction to Mathematics')
        self.assertEqual(self.course.instructor, 'Prof. Smith')

    def test_assignment_creation(self):
        # Test if the assignment was created successfully
        self.assertEqual(self.assignment.course, self.course)
        self.assertEqual(self.assignment.title, 'Homework 1')
        self.assertEqual(self.assignment.description, 'Complete exercises 1-5')
        self.assertEqual(self.assignment.deadline, '2024-02-28')
