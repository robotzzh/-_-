from django.db import models
import datetime
from django.utils import timezone
# Create your models here.



"""
insert polls_student values('1','xping','transgender','2002-1-1','chemistry');
"""

class test(models.Model):
    name = models.CharField(max_length=16)


class student(models.Model):
    sno = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=16)
    birth = models.CharField(max_length=16)
    majority = models.CharField(max_length=16)


"""
course表中记录老师姓名，编号，课程名
insert polls_course values('1','chemistry','lamo');
"""


class course(models.Model):
    cno = models.CharField(max_length=32, primary_key=True)
    cname = models.CharField(max_length=32)
    tutor = models.CharField(max_length=16)


"""
sc表，sno为主键，一个sno+cno组成一个确定一个成绩
"""


class sc(models.Model):
    no = models.AutoField(primary_key=True, default=1)
    sno = models.CharField(max_length=32)
    cno = models.CharField(max_length=32)
    credit = models.IntegerField()

    def __str__(self):
        return f'sno:{self.sno},cno:{self.cno},credit:{self.credit}'



