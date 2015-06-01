from django.db import models
from django_hstore import hstore
from django.contrib.postgres.fields import ArrayField

class Result(models.Model):
    result_name = models.CharField("Name", max_length=200, default="")
    result_usn = models.CharField("USN", max_length=10, default="", primary_key=True)
    result_sem = models.PositiveIntegerField("Semester", default=0)
    result_sgpa = models.FloatField("SGPA", default=0.0)
    result_branch = models.CharField("Branch", max_length=40, default="")
    result_sub = hstore.DictionaryField()

    objects = hstore.HStoreManager()


    def __unicode__(self):
        return '%s - %s' % (self.result_name, self.result_usn)

class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_code = models.CharField("SubCode", max_length=9, default="")
    sub_name = models.CharField("SubName", max_length=100, default="")
    sub_sem = models.PositiveIntegerField("SubSem", default=0)
    sub_branch = models.CharField("SubBranch", max_length=40, default="")

    def __unicode__(self):
        return '%s - %s' % (self.sub_name, self.sub_code)