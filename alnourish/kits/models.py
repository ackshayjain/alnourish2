from django.db import models


class Kits(models.Model):
    id = models.AutoField(primary_key=True)
    reg_number = models.BigIntegerField()

    is_registered = models.BooleanField(default=0)

    date_published = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id
