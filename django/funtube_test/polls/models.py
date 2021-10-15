from django.db import models

# Create your models here.
class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    total_vote_cnt = models.IntegerField(default=0)
    pop_time = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now=True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_id = models.IntegerField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    vote_cnt = models.IntegerField(default=0)