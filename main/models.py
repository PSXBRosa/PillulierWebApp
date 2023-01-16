from django.db import models
from django.conf import settings

def default_mode():
    return str({"SUN":False,
            "MON":False,
            "TUE":False,
            "WED":False,
            "THU":False,
            "FRY":False,
            "SAT":False})

class Machine(models.Model):
    name  = models.CharField(max_length=255, unique=True)
    pubk  = models.TextField(blank=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


class Drug(models.Model):
    name   = models.CharField(max_length=255, unique=True) # name given to the drug
    desc   = models.CharField(max_length=255, blank=True)  # description (optional)
    main_c = models.CharField(max_length=255, blank=True)  # main component (optional)
    fabr   = models.CharField(max_length=255, blank=True)  # fabricant (optional)
    presc_date = models.DateField(blank=True)              # prescription date (optional)


class Alarm(models.Model):
    name = models.CharField(max_length=255, unique=True)                    # name of the alarm
    cr_t = models.DateTimeField(auto_now_add=True)                          # time of creation of the alarm
    time = models.TimeField()                                               # time set for the alarm
    mode = models.TextField(default=default_mode)                           # mode of the alarm (e.g. 'SAT')
    mach = models.ForeignKey(Machine, on_delete=models.CASCADE)             # machine vinculated to the alarm
    meds = models.ManyToManyField(Drug, through="DrugsOnAlarm" ,blank=True) # drugs set for this alarm


class DrugsOnAlarm(models.Model):
    alarm = models.ForeignKey(Alarm, on_delete=models.CASCADE)
    drug  = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField()


