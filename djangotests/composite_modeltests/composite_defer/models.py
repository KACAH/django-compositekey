"""
Tests for defer() and only().
"""

from django.db import models
from compositekey import db

class Secondary(models.Model):
    id = db.MultiFieldPK("first","second")
    first = models.CharField(max_length=50)
    second = models.CharField(max_length=50)

class Primary(models.Model):
    id = db.MultiFieldPK("name","related")
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    related = models.ForeignKey(Secondary)

    def __unicode__(self):
        return self.name

class Child(Primary):
    pass

class BigChild(Primary):
    other = models.CharField(max_length=50)
