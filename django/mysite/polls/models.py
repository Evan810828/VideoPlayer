from django.db import models

# Create your models here.

class Vote(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Vote, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text