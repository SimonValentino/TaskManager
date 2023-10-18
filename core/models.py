from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=255, null=False)
    created_on = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"Task: {self.content}"