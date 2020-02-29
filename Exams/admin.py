from django.contrib import admin
from .models import Student,Exam,ExamQuestion,StudentAnswer
# Register your models here.

admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(ExamQuestion)
admin.site.register(StudentAnswer)
