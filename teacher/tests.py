from django.test import TestCase
import datetime
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse


class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data={
            "first_name" : "James",
            "last_name":"Mwai",
            "gender":"Male",
            "email" :"smartemwa@gmail.com",
            "phone_number":"0757451057",
            "profession":"Lecturer",
            "date_employed": datetime.date(2019,2,1),
            "subject_training":"python",
            "id_number":"12345",

        }

    
        self.bad_data={
            "first_name" : 43,
            "last_name":"Mwai",
            "gender":"Male",
            "email" :"smartemwagmailcom",
            "phone_number":"0757451057",
            "profession":"Lecturer",
            "date_employed ": "hello",
            "subject_training ":"python",
            "id_number":"12345",
        }


    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertTrue(form.is_valid())   

    def test_teacher_form_rejects_invalid_data(self):
        form=TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_teacher_view(self):
        client=Client()
        url=reverse("add_teacher")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200)

    def test_add_teacher_view_rejects_invalid_data(self):
        client=Client()
        url=reverse("add_teacher")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)




# Create your tests here.
