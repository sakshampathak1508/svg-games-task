from django.db import models
from django.utils import timezone
from datetime import date
from django.utils.translation import gettext as _
# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=256,blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    author = models.CharField(max_length=256,blank=True,null=True)
    published_date = models.DateField(_("Date"), default=date.today)
    
    def __str__(self):
        return self.name