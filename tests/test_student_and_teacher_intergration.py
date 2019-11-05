# from django.test import TestCase
# from teacher.models import Teacher
# from student.models import Student
# import datetime


# class StudentTeacherTestCase(TestCase):
#     def setUp(self):
#         self.student_a=Student.objects.create(
#             first_name="Philice",
#             last_name="Jumba",
#             date_of_birth=datetime.date(1995,12,20),
#             gender="Female",
#             registration_number="1234",
#             id="5837",
#             email="philicejumba@gmail.com",
#             phone_number="0771489931",
#             date_joined=datetime.date.today(),
#             )

#         self.student_b=Student.objects.create(
#             first_name="Gaya",
#             last_name="Gaya",
#             date_of_birth=datetime.date(1995,12,20),
#             gender="Female",
#             registration_number="4321",
#             id="4567",
#             email="gayaflo95@gmail.com",
#             phone_number="0771489831",
#             date_joined=datetime.date.today(),
#             )
            
#         self.teacher_a=Teacher.objects.create(
#             first_name= "James",
#             last_name="Mwai",
#             gender="Male",
#             email="smartemwa@gmail.com",
#             phone_number="0757451057",
#             profession="Lecturer",
#             date_employed= datetime.date(2019,2,1),
#             subject_training="python",
#             id_number="12345",


#             )
#         self.teacher_b=Teacher.objects.create(
#             first_name= "Orenge",
#             last_name="Anthony",
#             gender="Male",
#             email="antorenge@gmail.com",
#             phone_number="0757051057",
#             profession="Lecturer",
#             date_employed= datetime.date(2019,2,1),
#             subject_training="javascript",
#             id_number="34567",


#         )

#     def test_one_trainer_and_many_students_can_have_one_course(self):
#     	self.student_a.courses.add(self.python)
#     	self.student_b.courses.add(self.python)
#     	self.python.teacher = self.teacher_a



#     def test_one_trainer_and_many_students_can_have_many_courses(self):
#     	self.student_b.courses.add(self.python,self.javascript,self.electronics)
    	
                
