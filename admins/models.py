from django.db import models

class Admin(models.Model):
    identification = models.CharField(max_length = 50)
    password       = models.CharField(max_length = 200)

    class Meta:
        db_table = 'admins'
