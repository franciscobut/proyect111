from datetime import datetime
from email.policy import default
from tkinter.tix import Tree
from django.db import models

# Create your models here.
class empleado (models.Model):
    name=models.CharField(max_length=50,verbose_name='Nombres')
    curp=models.CharField(max_length=18,verbose_name='Curp')
    date_joined=models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_creation=models.DateField(auto_now=True)
    date_update=models.DateField(auto_now_add=True)
    age=models.PositiveIntegerField(default=0)
    salary=models.DecimalField(default=0.00,max_digits=5, decimal_places=2)
    state=models.BooleanField(default=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    cvitae=models.FileField(upload_to='cvitae/%Y/%m/%d',null=True,blank=True)

    
    class Meta:
        verbose_name = ("empleado")
        verbose_name_plural= ("empleados")
        db_table='empleado'
        ordering=['id']

        

    def __str__(self):
        return self.names

