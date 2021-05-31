from django.db import models

class User(models.Model):
    nickname    = models.CharField(max_length = 200)
    language    = models.ForeignKey('Language', on_delete = models.CASCADE)
    device_type = models.CharField(max_length = 50)

    class Meta:
        db_table = 'users'

class Language(models.Model):
    language_type = models.CharField(max_length = 20)
    movie_url     = models.CharField(max_length = 255)

    class Meta:
        db_table = 'languages'

