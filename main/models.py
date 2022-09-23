from django.db import models

# from rest_framework import serializers  # this is validation level(3)


# This function is for validation level(3)
'''def myFunc(value):
    if value < 18:
        raise serializers.ValidationError("age can not be less than 18 came from models")
    else:
        return value
'''


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    # age = models.IntegerField(default=18, validators=[myFunc])   # this is for validation level(3)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
