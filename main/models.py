from django.db import models

# Create your models here.
class path(models.Model):
    url=models.CharField(max_length=1000)
    url_short=models.CharField(max_length=50)
    class meta:
        db_table = 'path'