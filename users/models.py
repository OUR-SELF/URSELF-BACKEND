from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser이기 때문에 코드에서만 쓰이고 DB에 저장 X
# => 'Abstract' Model

class Users(AbstractUser):
    """ Base User Model """

    USERTYPE_CONSUMER = "consumer"
    USERTYPE_COMPANY = "company"

    USERTYPE_CHOICES = (
        (USERTYPE_CONSUMER, "consumer"),
        (USERTYPE_COMPANY, "company"),
    )
    
    profile_img = models.ImageField(default="default-img.png", null=True)
    usertype = models.CharField(max_length=8,choices=USERTYPE_CHOICES)
    name = models.CharField(max_length=50)
    address_num = models.CharField(max_length=30)
    address_road = models.CharField(max_length=100)
    address_detail = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)

    # 물리적으로 존재하지 않는 astract 상태
    class meta:
        abstract = True


class Consumer_Users(Users):
  """ Consumer User Model """
  
  GENDER_MALE = "male"
  GENDER_FEMALE = "female"

  GENDER_CHOICES = (
      (GENDER_MALE, "Male"),
      (GENDER_FEMALE, "Female"),
  )
  # gender를 선택권을 주는 CharField로 수정하기 위한 튜플 => choices 파라미터에 이용
  # GENDER_MALE 값이 DB에 저장되고, "Male"은 (admin)form에서 보여지는 값

  # blank=True의 경우 form에도 적용되어 값을 필수로 채우지 않아도 됨
  # null=True는 DB에서만 사용됨
  gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
  age = models.IntegerField()

  class Meta:
    verbose_name = "Consumer User"
  # 관리자 화면에 보기 편하게 표시하기 위한 설정


class Company_Users(Users):

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

  category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
  homepage_link = models.CharField(blank=True, max_length=500)
  subscribe_count = models.IntegerField(default=0)
  

