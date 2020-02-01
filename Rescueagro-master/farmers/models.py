from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Farmer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_farmer")
    quantity = models.PositiveIntegerField(default = 0)
    crop_name = models.CharField(max_length = 120)
    TIME_CHOICES = (
        ('m_1', '1 Month'),
        ('m_3', '3 Months'),
        ('m_6', '6 Month'),
        ('m_12', '12 Month'),
    )
    time_type = models.CharField(max_length=3, choices=TIME_CHOICES)
    on_hold = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} {self.crop_name} {self.time_type} "
