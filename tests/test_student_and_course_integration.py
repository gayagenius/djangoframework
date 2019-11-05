from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime


class StudentCourseTestCase(TestCase):
    def setUp(self):
        self.student_a=Student.objects.create(
            first_name="Rosephillice",
            last_name="Jumba",
            date_of_birth=datetime.date(1995,12,20),
            gender="Female",
            registration_number="1234",
            id="5837",
            email="philicejumba@gmail.com",
            phone_number="0771489931",
            date_joined=datetime.date.today(),
            )
        self.student_b=Student.objects.create(
            first_name="Gaya",
            last_name="Gaya",
            date_of_birth=datetime.date(1995,12,20),
            gender="Female",
            registration_number="4321",
            id="4567",
            email="gayaflo95@gmail.com",
            phone_number="0771489831",
            date_joined=datetime.date.today(),
            )

        self.javascript=Course.objects.create(
             name="JavaScript",
             duration_in_months=10,
             start_date=datetime.date(2019,2,1),
             end_date=datetime.date(2019,12,1),
             course_description="FrontEnd development",
        )

        self.python=Course.objects.create(
             name="python",
             duration_in_months=10,
             start_date=datetime.date(2019,2,1),
             end_date=datetime.date(2019,12,1),
             course_description="BackendEnd development",
        )

        self.electronics=Course.objects.create(
             name="C++",
             duration_in_months=10,
             start_date=datetime.date(2019,2,1),
             end_date=datetime.date(2019,12,1),
             course_description="Arduino development",
        )

    def test_student_can_join_a_course(self):
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(),1)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(),2)
        self.student_a.courses.add(self.electronics)
        self.assertEqual(self.student_a.courses.count(),3)


    def test_student_can_join_many_courses(self):
        self.student_b.courses.add(self.python,self.javascript,self.electronics)
        self.assertEqual(self.student_b.courses.count(),3)

     

        
