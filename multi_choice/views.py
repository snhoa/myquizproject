from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import multi_choice
from .serializers import mcSerializer
import random

# Create your views here.

@api_view(['GET'])
def showQuiz(request):
    totalQuizs = multi_choice.objects.all()
    serializer = mcSerializer(totalQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomQuiz(requser):
    totalQuizs = multi_choice.objects.all()
    count = totalQuizs.count()
    randomQuiz = random.sample(list(totalQuizs),count)
    serializer = mcSerializer(randomQuiz, many=True)
    return Response(serializer.data)

#1과목 
@api_view(['GET'])
def Subject_1_1(request):
    totalQuizs = multi_choice.objects.filter(subject = "소프트웨어설계/요구사항확인")
    serializer = mcSerializer(totalQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Subject_1_2(request):
    totalQuizs = multi_choice.objects.filter(subject = "소프트웨어설계/화면설계")
    serializer = mcSerializer(totalQuizs, many=True)
    return Response(serializer.data)@api_view(['GET'])

@api_view(['GET'])
def Subject_1_3(request):
    totalQuizs = multi_choice.objects.filter(subject = "소프트웨어설계/애플리케이션설계")
    serializer = mcSerializer(totalQuizs, many=True)
    return Response(serializer.data)@api_view(['GET'])

@api_view(['GET'])
def Subject_1_4(request):
    totalQuizs = multi_choice.objects.filter(subject = "소프트웨어설계/인터페이스설계")
    serializer = mcSerializer(totalQuizs, many=True)
    return Response(serializer.data)@api_view(['GET'])

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")
