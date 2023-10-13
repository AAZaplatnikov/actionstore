from django.db import models

class Floor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ActionStore(models.Model):
    actionSt_dt = models.DateTimeField(auto_now=True)
    action_zone = models.CharField(max_length=100)
    Action_tipe = models.CharField(max_length=100)
    numbers_clips = models.CharField(max_length=100)
    cost= models.CharField(max_length=100)
    # storenumber = models.CharField(max_length=100, default='default_value')
    # datestore = models.DateTimeField(default='2023-01-01 00:00')
    # timestore = models.CharField(max_length=100,default='default_value',)
    # floor = models.ForeignKey(Floor, on_delete=models.CASCADE,default='default_value')

    def __str__(self):
        return f"{self.action_zone} - {self.Action_tipe}"



