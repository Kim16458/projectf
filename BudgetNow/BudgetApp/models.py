from django.db import models

# Create your models here.

class Categories(models.Model):
   
   TYPE_CHOICES = [
      ('expense', 'Expense'),
      ('budget', 'Budget'),
      ('both', 'Both')
   ]
   CategoryID = models.AutoField(primary_key=True)
   CategoryName = models.CharField(max_length=100, unique=True)
   BudgetLimit = models.IntegerField()
   ParentID = models.IntegerField()
   CategoryType = models.CharField(max_length=10, choices=TYPE_CHOICES,default='expense')

   def __str__(self):
      return f"{self.CategoryName} - {self.CategoryType}"

class Expense(models.Model):
   ID = models.AutoField(primary_key=True)
   Description = models.CharField(max_length=100) 
   Category = models.CharField(max_length=100)
   Amount = models.IntegerField()
   Date = models.DateField()
   CategoryID = models.ForeignKey(Categories,to_field='CategoryID', on_delete=models.CASCADE, null=True)

   def __str__(self):
      return f"{self.Category} - {self.Amount}"
   
class Budget(models.Model):
   BudgetID = models.AutoField(primary_key=True)
   CategoryName = models.CharField(max_length=100)
   TimeInMonths = models.IntegerField()
   Maximum = models.IntegerField(default=0)
   CategoryID = models.ForeignKey(Categories,to_field='CategoryID', on_delete=models.CASCADE, null=True)

   def __str__(self):
      return f"{self.CategoryName} - {self.Maximum} - {self.TimeInMonths}"
