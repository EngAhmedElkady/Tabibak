from django.db import models
# Create your models here.


class Heart(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    age =models.DecimalField(max_digits=20,decimal_places=2)
    cp =models.DecimalField(max_digits=20,decimal_places=2)
    trestbps =models.DecimalField(max_digits=20,decimal_places=2)
    chol =models.DecimalField(max_digits=20,decimal_places=2)
    thalach =models.DecimalField(max_digits=20,decimal_places=2)
    exang =models.DecimalField(max_digits=20,decimal_places=2)
    oldpeak =models.DecimalField(max_digits=20,decimal_places=2)
    ca =models.DecimalField(max_digits=20,decimal_places=2)
    result=models.IntegerField(null=True ,blank=True,default=0)
    result2=models.IntegerField(null=True ,blank=True,default=0)

    