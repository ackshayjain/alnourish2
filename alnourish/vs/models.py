from django.db import models

#
# Create your models here.
class Contact(models.Model):

    id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    comments = models.CharField(max_length=200)
    # volume = models.IntegerField()
    #
    # test_date = models.CharField(max_length = 200,default='')
    # ph_test = models.CharField(max_length=200,default='')

    date_published = models.DateTimeField(auto_now_add=True)
    # end_date = models.DateTimeField(default=datetime.now() + timedelta(days=15))

    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
