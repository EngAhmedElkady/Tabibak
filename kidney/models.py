from django.db import models
from django.utils import timezone


class Kidney(models.Model):
    
    choice=(
        ("yes","yes"),
        ("no","no")
    )
    
    date=models.DateTimeField(auto_now_add=True)
    age =models.DecimalField(max_digits=4,decimal_places=2)
    al=models.IntegerField()
    su =models.DecimalField(max_digits=4,decimal_places=2)
    bgr=models.IntegerField(verbose_name=("blood glucose random"))
    bu=models.IntegerField(verbose_name=("blood urea"))
    sc=models.DecimalField(max_digits=4,decimal_places=2,verbose_name=("serum creatinine"))
    hemo=models.DecimalField(max_digits=4,decimal_places=2,verbose_name=("haemoglobin"))
    pcv=models.IntegerField(verbose_name=("packed cell volume"))
    wc=models.IntegerField(verbose_name=("white blood cell count"))
    htn=models.CharField(max_length=100,choices=choice, verbose_name=("ypertension"))
    result=models.IntegerField(null=True ,blank=True,default=0)
    result2=models.CharField(max_length=50,null=True ,blank=True,default=0)
    
    
