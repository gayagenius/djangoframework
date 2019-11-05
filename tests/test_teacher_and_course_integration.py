from django.test import TestCase
from teacher.models import Teacher
from course.models import Course
import datetime

class TeacherCourseTestCase(TestCase):
    def setUp(self):
        self.teacher_a=Teacher.objects.create(
            first_name= "James",
            last_name="Mwai",
            gender="Male",
            email="smartemwa@gmail.com",
            phone_number="0757451057",
            profession="Lecturer",
            date_employed= datetime.date(2019,2,1),
            subject_training="python",
            id_number="12345",


            )
        self.teacher_b=Teacher.objects.create(
            first_name= "Orenge",
            last_name="Anthony",
            gender="Male",
            email="antorenge@gmail.com",
            phone_number="0757051057",
            profession="Lecturer",
            date_employed= datetime.date(2019,2,1),
            subject_training="javascript",
            id_number="34567",


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


    def test_course_can_have_a_single_teacher(self):
        self.python.teacher = self.teacher_a
        self.assertEqual(self.python.teacher, self.teacher_a)

    def test_many_courses_can_be_trained_by_one_trainer(self):
       self.python.teacher = self.teacher_b
       self.javascript.teacher = self.teacher_b
       self.assertEqual(self.javascript.teacher,self.python.teacher)