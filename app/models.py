from django.db import models

# Create your models here.

class Data(models.Model):
    data_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.data_name

class Web(models.Model):
    data_name=models.ForeignKey(Data,on_delete=models.CASCADE)
    web_name=models.CharField(max_length=100)
    web_subject=models.CharField(max_length=100)
    web_data=models.CharField(max_length=100)

    def __str__(self):
        return self.web_name
    
