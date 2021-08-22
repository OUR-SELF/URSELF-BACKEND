from django.db import models
from users import models as user_models

# Create your models here.
class Subscribes(models.Model):
  # company or consumer 모두 저장될 수 있음
  consumer = models.ForeignKey(user_models.Consumer_Users, on_delete=models.CASCADE, null=True)
  company = models.ForeignKey(user_models.Company_Users, on_delete=models.CASCADE, null=True)