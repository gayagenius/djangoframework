from django.test import TestCase
import datetime
from course.forms import CourseForm
from django.test import Client
from django.urls import reverse

class AddCourseTestCase(TestCase):
    def setUp(self):
        self.data={
             "name":"JavaScript",
             "duration_in_months":10,
             "start_date":datetime.date(2019,2,1),
             "end_date":datetime.date(2019,12,1),
             "course_description":"FrontEnd development",
        }

        self.bad_data={
             "name":"JavaScript",
             "duration_in_months":10,
             "start_date":datetime.date(2019,2,1),
             "end_date":"hello",
             "course_description":"FrontEnd development",
             "teacher":"James Mwai",
        }

    def test_course_form_accepts_valid_data(self):

        form = CourseForm(self.data)
        self.assertTrue(form.is_valid())   

    def test_course_form_rejects_invalid_data(self):
        form=CourseForm(self.bad_data)
        self.assertFalse(form.is_valid())


    def test_add_course_view(self):
        client=Client()
        url=reverse("add_course")
        response=client.post(url,self.data)
        self.assertEqual(response.status_code,200)

    def test_add_course_view_rejects_invalid_data(self):
        client=Client()
        url=reverse("add_course")
        response=client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)



        



# Create your tests here.
