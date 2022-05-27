from django.db import models
from UsersApp.models import CustomUser

class Bugs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    reporter = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True)
    current_status = models.CharField(max_length=30)
    severity = models.CharField(max_length=30)

    def __str__(self):
        return self.title