from django.db import models

# Create your models here.

class RequestData(models.Model):    
    url = models.URLField()
    convert_from = models.CharField(max_length=10,blank=True,null=True)
    convert_to = models.CharField(max_length=10,blank=True,null=True)
    amount = models.FloatField(blank=True,null=True)
    datetime = models.DateTimeField()
    response_body = models.TextField(blank=True,null=True)
    
    class Meta:    
        db_table = 'request_data'
        verbose_name = 'Request Data'
        verbose_name_plural = 'Request Data'