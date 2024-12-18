from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.PositiveSmallIntegerField()  # Options: 1, 2, 3, 4

    def __str__(self):
        return self.question_text
