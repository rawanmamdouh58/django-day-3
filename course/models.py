from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='course/img', default='dina.png')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name