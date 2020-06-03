from django.db import models

# Create your models here.

class ManageQuestion(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=2)


class Test(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    subject=models.CharField(max_length=60)
    timer=models.CharField(max_length=4)
    password=models.CharField(max_length=20)

class TestQuestion(models.Model):
    queId=models.ForeignKey(ManageQuestion,on_delete=models.CASCADE)
    testId=models.ForeignKey(Test,on_delete=models.CASCADE)

class QuizResult3(models.Model):
    rollno=models.CharField(max_length=10)

class QuizResult(models.Model):
    rollno=models.CharField(max_length=10)
    testId=models.CharField(max_length=30)
    marks=models.CharField(max_length=3)




