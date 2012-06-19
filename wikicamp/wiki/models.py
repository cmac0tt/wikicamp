from django.db import models
#from django.core.files import File
# Create your models here.

#class Tag(models.Model):
#    name = models.CharField(max_length = "20", primary_key = True)
 
#class Page(models.Model):
#    name = models.CharField(max_length="45", primary_key = True)
#    content = models.TextField(blank=True)
#    pub_date = models.DateTimeField('date published')
#    tags = models.ManyToManyField(Tag)
#    def __unicode__(self):
#        return self.name

class Page(models.Model):
	name = models.CharField(max_length="20", primary_key=True)
	content = models.TextField(blank=True)
def __unicode__(self):
	return self.name



	
