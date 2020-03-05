from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField()
    mobile_no = models.CharField(max_length=13)
    Class = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    stream = models.CharField(max_length=20)
    created_date = models.DateField()
    updated_date = models.DateField()
    

class Exam(models.Model):
    Institute_name = models.CharField(max_length=200)
    stream = models.CharField(max_length=20)
    Class  = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    exams_Id = models.IntegerField()
    created_date = models.DateField()
    updated_date = models.DateField()
    

class ExamQuestion(models.Model):
    exams_Id = models.ForeignKey(Exam,on_delete=models.CASCADE)
    Question = models.ImageField()
    Answer = models.CharField(max_length=20)
    created_date = models.DateField()
    updated_date = models.DateField()
    exam_question_id = models.IntegerField()


class StudentAnswer(models.Model):
    email = models.EmailField()
    exam_question_id = models.ForeignKey(ExamQuestion,on_delete=models.CASCADE)
    Answer_given = models.CharField(max_length=20)
    Correct_Answer = models.IntegerField()
    Score = models.IntegerField()
    created_date = models.DateField()
    updated_date = models.DateField()


    def save(self, *args, **kwargs):
        print(self)
        if self.Answer_given == self.exam_question_id.Answer:
            self.Score = self.Score + 1
        super(StudentAnswer, self).save(*args, **kwargs)







