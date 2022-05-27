import resource
from django.db import models
from BugsApp.models import Bugs
from UsersApp.models import CustomUser

# Create your models here.
class Relation(models.Model):
    bugId = models.ForeignKey(Bugs, on_delete=models.CASCADE)
    assignedTo = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resource')
    assignedBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assignedOn = models.DateField(auto_now_add=True)
    statusRightNow = models.CharField(max_length=10)

