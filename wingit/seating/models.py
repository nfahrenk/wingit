from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.postgres.fields import ArrayField
from LINKEDIN_OPTIONS import INDUSTRY_CHOICES
from MovieRecommendation import MovieRecommender
import os

class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    ind = models.IntegerField(_("Industry"), choices=INDUSTRY_CHOICES)
    prefersBusiness = models.BooleanField(_("Prefers Business?"), default=False)
    likes = ArrayField(models.CharField(max_length=20))
    twitter_handle = models.CharField(_("Twitter Handle"), max_length=15, blank=True)

    def getIndustry(self):
        return dict(INDUSTRY_CHOICES)[self.ind]
    
    def getMood(self):
        if self.twitter_handle:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            path = os.path.join(BASE_DIR, "seating/delta_movies.xlsx")
            x = MovieRecommender(path)
            try:
                return x.getMovie(x.getData(), self.twitter_handle)        
            except Exception:
                return None
        else:
            return None

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name.lower()+"_"+self.last_name.lower()
    
    def __unicode__(self):
        return str(self)

    def get_img(self):
        return str(self)