from django.db import models
from courses.models import Course
class Quiz(models.Model):
    question = models.CharField(max_length=500, null=False, default='')
    option1 = models.CharField(max_length=100, null=False, default='')  
    option2 = models.CharField(max_length=100, null=False, default='')  
    option3 = models.CharField(max_length=100, null=False, default='')  
    option4 = models.CharField(max_length=100, null=False, default='')  
    answer = models.IntegerField(null = False,default=0)  

    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    week_id = models.IntegerField(default = 0)
    is_preview = models.BooleanField(default = False)
    def __str__(self):
        return self.question

    




    