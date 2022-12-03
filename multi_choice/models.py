from django.db import models

# Create your models here.
class multi_choice(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length = 20)      # 과목
    title = models.CharField(max_length = 200)       # 문제
    body = models.TextField()                        # 4지선다
    answer = models.IntegerField()                   # 정답
    image = models.ImageField(upload_to='profile/', null=True, blank=True) #이미지
    date = models.CharField(max_length = 10)         # 날짜
    explanation = models.TextField()                 # 해설