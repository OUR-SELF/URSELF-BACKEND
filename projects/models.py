from django.db import models
from users import models as user_models

# Create your models here.
class Project(models.Model):

  CATEGORY_GAME = "game"
  CATEGORY_FOOD_LIVING = "food/living"
  CATEGORY_FASHION_ACCS = "fashion accessories"
  CATEGORY_CRAFTS = "crafts"
  CATEGORY_ETC = "etc"

  CATEGORY_CHOICES = (
      (CATEGORY_GAME, "Game"),
      (CATEGORY_FOOD_LIVING, "Food/Living"),
      (CATEGORY_FASHION_ACCS, "Fashion Accessories"),
      (CATEGORY_CRAFTS, "Crafts"),
      (CATEGORY_ETC, "ETC")
  )

  # company or consumer 모두 저장될 수 있음
  user = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, null=True)
  name = models.CharField(max_length=100)
  category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
  end_date = models.DateField(null=False)
  matched = models.BooleanField(default=False)
  liked = models.IntegerField(default=0)

  price = models.IntegerField()
  target_amount = models.IntegerField(default=0)
  target_count = models.IntegerField(default=0)

  comment = models.CharField(max_length=50)
  intent = models.CharField(max_length=800)
  details = models.CharField(max_length=3000)
  counted_user_num = models.IntegerField(default=0)

  thumbnail_image = models.ImageField(blank=True, null=True)
  detail_image = models.ImageField(blank=True, null=True)


