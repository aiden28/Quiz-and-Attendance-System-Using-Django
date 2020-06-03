from django.contrib import admin
from .models import ManageQuestion, Test, TestQuestion,QuizResult,QuizResult3
# Register your models here.

admin.site.register(ManageQuestion)
admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(QuizResult)
admin.site.register(QuizResult3)