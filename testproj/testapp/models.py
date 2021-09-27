from django.db import models


class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    has_middle_name = models.BooleanField(default=False)

    def __str__(self):
        return self.name
