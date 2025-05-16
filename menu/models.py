from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                               null=True, blank=True, related_name='children')
    def __str__(self):
        return self.name

