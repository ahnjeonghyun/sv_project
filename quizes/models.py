from django.db import models

class Quiz(models.Model):
    content     = models.CharField(max_length = 1000) 
    language    = models.ForeignKey('users.Language', on_delete = models.CASCADE)
    quiz_seq    = models.IntegerField()
    reward      = models.ForeignKey('Reward', on_delete = models.PROTECT)

    class Meta:
        db_table = 'quizes'

class UserAnswer(models.Model):
    user      = models.ForeignKey('users.User', on_delete = models.CASCADE)
    quiz      = models.ForeignKey('Quiz', on_delete = models.CASCADE)
    is_answer = models.BooleanField(null = True)

    class Meta:
        db_table = 'user_answers'

class Answer(models.Model):
    answer_seq    = models.SmallIntegerField()
    answer        = models.CharField(max_length = 255)
    answer_status = models.BooleanField(default = False ,blank = False)
    quiz          = models.ForeignKey('Quiz', on_delete = models.CASCADE)
    language      = models.ForeignKey('users.Language', on_delete = models.CASCADE)

    class Meta:
        db_table = 'answers'

class Reward(models.Model):
    reward_rate        = models.DecimalField(max_digits = 3, decimal_places = 2)
    mobile_image_url   = models.CharField(max_length = 255)
    pc_image_url       = models.CharField(max_length = 255)
    mobile_reward_name = models.CharField(max_length = 100)
    pc_reward_name     = models.CharField(max_length = 100)
    language           = models.ForeignKey('users.Language', on_delete = models.CASCADE)

    class Meta:
        db_table = 'rewards'
