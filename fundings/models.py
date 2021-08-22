from django.db import models
from users import models as user_models
from projects import models as project_models

# Create your models here.
class Funding(models.Model):
  consumer = models.ForeignKey(user_models.Consumer_Users, on_delete=models.CASCADE, null=True)
  project = models.ForeignKey(project_models.Project, on_delete=models.CASCADE, null=True)