from django.db import models

# Create your models here.
class Subject(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Chapter(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    name = models.CharField(max_length=256)

    class YearTextChoice(models.TextChoices):
        MP2I = "1", "MP2I"
        MPI  = "2", "MPI"
    year = models.CharField(
        max_length=1,
        choices=YearTextChoice.choices,
        default=YearTextChoice.MP2I
    )

    def __str__(self):
        return self.subject.name.upper() + " " + self.name + " (" + self.get_year_display() + ")"

class Question(models.Model):

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
