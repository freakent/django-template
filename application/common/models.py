from django.db import models
from django.conf import settings

# Create your models here.

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    created_by = models.CharField(default="ANON")

    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.CharField(default="ANON")

    class Meta:
        abstract = True