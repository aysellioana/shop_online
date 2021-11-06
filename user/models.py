from django.contrib.auth.models import User
from django.db import models

class ExtendUser(User):
    date_of_birth = models.DateField()
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
