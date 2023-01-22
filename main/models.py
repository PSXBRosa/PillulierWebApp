from django.db import models
from django.conf import settings


class Drug(models.Model):
    name   = models.CharField(max_length=255, unique=True) # name given to the drug
    desc   = models.CharField(max_length=255, null=True, blank=True)  # description (optional)
    main_c = models.CharField(max_length=255, null=True, blank=True)  # main component (optional)
    fabr   = models.CharField(max_length=255, null=True, blank=True)  # fabricant (optional)
    presc_date = models.DateField(null=True, blank=True)              # prescription date (optional)

class Alarm(models.Model):
    name = models.CharField(max_length=255, unique=True)                        # name of the alarm
    cr_t = models.DateTimeField(auto_now_add=True)                              # time of creation of the alarm
    mode = models.TextField(null=True, blank=True)                              # Aditional information
    time = models.DateTimeField()                                               # time set for the alarm
    meds = models.ManyToManyField(Drug, through="DrugsOnAlarm" , null=True, blank=True) # drugs set for this alarm


class DrugsOnAlarm(models.Model):
    alarm = models.ForeignKey(Alarm, on_delete=models.CASCADE)
    drug  = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField()


