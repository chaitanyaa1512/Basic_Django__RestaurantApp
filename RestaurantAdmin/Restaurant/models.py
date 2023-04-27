from django.db import models

# Create your models here.


class Food(models.Model):
    mainStreamFoodName=models.CharField(max_length=200)
    subCategoryFoodCharge=models.IntegerField()
   

    def __str__(self):
        return self.mainStreamFoodName
    
class Tables(models.Model):
    tableName=models.CharField(max_length=200)
   
    def __str__(self):
        return self.tableName
    
    
class Waiters(models.Model):
    waiterName=models.CharField(max_length=200)
   

    def __str__(self):
        return self.waiterName
    
    
class Orders(models.Model):
    foodName=models.CharField(max_length=200)
    foodPrice=models.IntegerField()
    nameOfTable=models.CharField(max_length=200)
    nameOfWaiter=models.CharField(max_length=200)
   

    def __str__(self):
        return self. foodName