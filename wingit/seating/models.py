from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    industry = models.CharField(max_length=50)
    prefersBusiness = models.BooleanField(_("Prefers Business?"), default=False)
    likes = ArrayField(models.CharField(max_length=20))
    twitter_handle = models.CharField(_("Twitter Handle"), max_length=15, blank=True)

    def getMood(self):
        return 1

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name.lower()+"_"+self.last_name.lower()
    
    def __unicode__(self):
        return str(self)

    def get_img(self):
        return str(self)