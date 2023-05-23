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
    class LeadReason(models.IntegerChoices):
        TELEVISION = 1, "TV"
        RADIO = 2, "Radio"
        INTERNET = 3, "Internet"
        PERSONAL = 4, "Personal"
        OTHER = 5, "Other"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    lead_reason = models.PositiveSmallIntegerField(choices=LeadReason.choices, default=LeadReason.INTERNET)
    lead_reason_other = models.CharField(max_length=50, blank=True)

    has_profile_picture = models.BooleanField(default=False)
    profile_picture = models.FileField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
