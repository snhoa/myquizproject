from rest_framework import serializers
from .models import multi_choice

# 모델 데이터가 주어지면 JSON 데이터로 변환해준다.
class mcSerializer(serializers.ModelSerializer):
    class Meta:
        model = multi_choice
        fields = ('id','subject', 'title', 'body', 'answer', 'image', 'date', 'explanation')

