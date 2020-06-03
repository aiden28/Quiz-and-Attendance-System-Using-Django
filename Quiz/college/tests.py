
from django.test import TestCase
from college.models import Dept, Class
# Create your tests here.


class InfoTest(TestCase):


    # Create your tests here.

    def create_dept(self, id='CS', name='CS'):
        return Dept.objects.create(id=id, name=name)