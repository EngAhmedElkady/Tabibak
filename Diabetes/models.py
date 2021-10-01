from django.db import models
# Create your models here.

#[Pregnancies , Glucose , SkinThickness , Insulin , Age]
class Diabets(models.Model):
    age =models.DecimalField(max_digits=20,decimal_places=2)
    date=models.DateTimeField(auto_now_add=True)
    Pregnancies=models.IntegerField()
    Glucose=models.IntegerField()
    SkinThickness=models.IntegerField()
    Insulin=models.IntegerField()
    result=models.IntegerField(null=True ,blank=True,default=0)
    result2=models.IntegerField(null=True ,blank=True,default=0)

    