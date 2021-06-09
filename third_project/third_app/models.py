from django.db import models

# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    profession = models.CharField(max_length = 25)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Job(models.Model):
    job_holder = models.ForeignKey(People, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    joine_date = models.DateField()

    ratting = (
        (1, 'Worst'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excelent')
    )
    performance = models.IntegerField(choices = ratting)
    def __str__(self):
        return self.name+" ratting: "+str(self.performance)
