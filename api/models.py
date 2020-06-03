from django.db import models

# Create your models here.
class Task(models.Model):
    content = models.CharField(max_length=255, null=True)
    complete = models.BooleanField(default=False, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content