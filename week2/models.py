from django.db import models

# Create your models here.
class Questions(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Choice(models.Model):
        questtion = models.ForeignKey(Questions,on_delete=models.CASCADE )
        choice_text = models.CharField(max_length=3)
        Votes = models.IntegerField(default=0)

        def __str__(self):
            return self.choice_text
        