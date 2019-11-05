from django.test import TestCase
from .models import Student
import datetime
from student.forms import StudentForm
from django.test import Client
from django.urls import reverse

class StudentTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name="Evelyn",
            last_name="Kyengo",
            date_of_birth=datetime.date(1995,12,20),
            gender="Fluid",
            registration_number="1234",
            email="gayaflo95@gmail.com",
            phone_number="0771489831",
            date_joined=datetime.date.today(),
            )
    def test_full_name_contains_first_name(self):
            self.assertIn(self.student.first_name,self.student.full_name())
    def test_full_name_contains_last_name(self):
            self.assertIn(self.student.last_name,self.student.full_name())

    def test_age_is_always_above_17(self):
        self.assertFalse(self.student.clean() < 17 )

    def test_age_is_always_below_30(self):
        self.assertFalse(self.student.clean() > 30 )




class AddStudentTestCase(TestCase):
    def setUp(self):
        self.data={
        "first_name":"James",
        "last_name":"Mwai",
        "date_of_birth":datetime.date(1995,12,20),
        "gender":"male",
        "registration_number":"4837",
        "email":"smartemwa@gmail.com",
        "phone_number":"0771489831",
        "date_joined":datetime.date.today(),
        }

    
        self.bad_data={
        "first_name":"James",
        "last_name":"Mwai",
        "date_of_birth":datetime.date(1995,12,20),
        "gender":"male",
        "registration_number":"4837",
        "email":"smartemwagmail",
        "phone_number":"0771489831",
        "date_joined":datetime.date.today(),

        }

    def test_student_form_accepts_valid_data(self):
        form = StudentForm(self.data)
        self.assertTrue(form.is_valid())   

    def test_student_form_rejects_invalid_data(self):
        form=StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())



    def test_add_student_view(self):
        client=Client()
        url=reverse("add_student")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200)

    def test_add_student_view_rejects_invalid_data(self):
        client=Client()
        url=reverse("add_student")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)



        
            

# Create your tests here.
