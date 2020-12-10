import  os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudProject.settings')
import django
django.setup()

from crudApp.models import *
from faker import  Faker
from random import *
faker=Faker()

def populate(n) :
    for i in range(n) :
        feno=randint(1,999)
        fename=faker.name()
        fesal=randint(12000,30000)
        feaddr=faker.city()
        emp_record=Emp.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
populate(20)