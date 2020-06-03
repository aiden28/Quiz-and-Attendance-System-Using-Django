from django.contrib import admin
from .models import Student
from .models import Student,Class,Stream,Teacher,Attendance,Fee
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Fee)



class ClassInline(admin.TabularInline):
    model = Class
    extra = 0





class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'dept', 'section')
    search_fields = ('id', 'dept__name', 'section')
    ordering = ['dept__name', 'section']
    #inlines = [StudentInline]



admin.site.register(Student)
admin.site.register(Class,ClassAdmin)
admin.site.register(Stream)