from django.db import models

# week 1
class Hello(models.Model):
    # Column called 'text' with a maximum length of 200 characters
    text = models.CharField(max_length=200)
    
# Week 2
class Person(models.Model):
    # Columns for name and age
    # pk is auto created and incremented once a new row is created, that's why not defined here
    name = models.CharField(max_length=500, null=False, blank=False, db_index=True)
    age = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Address(models.Model):
    number = models.IntegerField(null=False, blank=False)
    street_name = models.CharField(max_length=500, null=False, blank=True)
    # Foreign key to Person model, allowing null values and setting to null if the referenced Person is deleted
    resident = models.ForeignKey(Person, on_delete=models.SET_NULL)