from django.db import models
from course.models import Course
# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, default='dina@gmail.com')
    image = models.ImageField(upload_to='trainee/img', default='dina.png')
    status = models.BooleanField(default=True)

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        related_name='trainees'
    )

    def __str__(self):
        return self.name