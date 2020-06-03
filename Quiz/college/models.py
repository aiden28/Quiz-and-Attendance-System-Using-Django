from django.db import models

# Create your models here.

class Stream(models.Model):
     name=models.CharField(max_length=20,primary_key=True)

     def __str__(self):
          return self.name


class Class(models.Model):
     id=models.CharField(primary_key=True,max_length=5)
     dept = models.ForeignKey(Stream, on_delete=models.CASCADE)
     name=models.CharField(max_length=2)
     section=models.CharField(max_length=2)

     class Meta:
          verbose_name_plural = 'classes'
     def __str__(self):
          d = Stream.objects.get(name=self.dept)
          return '%s %s %s %s' % (self.id,d.name,self.name,self.section)


class Student(models.Model):
     class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
     name=models.CharField(max_length=30)
     fatherName=models.CharField(max_length=30)
     motherName=models.CharField(max_length=30)
     address=models.TextField()
     Class=models.IntegerField()
     section = models.CharField(max_length=2)
     prevClass=models.IntegerField()
     prevClassMark=models.IntegerField()
     prevResult=models.ImageField(upload_to='images')
     gender=models.CharField(max_length=6)
     image=models.ImageField(upload_to='images')
     department=models.CharField(max_length=20)
     dob=models.CharField(max_length=10)
     password=models.CharField(max_length=30)
     rollno=models.CharField(max_length=10)


class Attendance(models.Model):
     rollno=models.ForeignKey(Student,on_delete=models.CASCADE)
     class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
     date=models.CharField(max_length=11)
     status=models.CharField(max_length=7)



class Teacher(models.Model):
     id=models.CharField(max_length=20,primary_key=True)
     name=models.CharField(max_length=30)
     fatherName = models.CharField(max_length=30)
     motherName = models.CharField(max_length=30)
     address=models.CharField(max_length=200)
     mono=models.IntegerField()
     qualification=models.TextField()
     gender=models.CharField(max_length=10)
     image=models.ImageField(upload_to='images')
     dob=models.CharField(max_length=10)
     email=models.EmailField()
     password = models.CharField(max_length=25)

class Fee(models.Model):
     rollno=models.CharField(max_length=10)
     class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
     amount=models.CharField(max_length=6)
     orderId=models.CharField(max_length=40)
     txnId= models.CharField(max_length=40)
     bankTxnId=models.CharField(max_length=10)
     txnDate=models.CharField(max_length=30)
     mode=models.CharField(max_length=10)
     status=models.CharField(max_length=10)














