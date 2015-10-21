from django.db import models
from django.core.exceptions import ValidationError

class Inventory(models.Model):
    """
    An inventory containing computers.
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

def inv_unique(iname):
    return Inventory.objects.filter(name__exact==iname).empty()


class Computer(models.Model):
    """
    A computer inventory entry, containing a serial number, manufacturer name,
    inventory, and comments.
    """
    inv = models.ForeignKey(Inventory)
    sn = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    comments = models.TextField()

    def __unicode__(self):
        return unicode(self.manufacturer + " " + self.sn)
