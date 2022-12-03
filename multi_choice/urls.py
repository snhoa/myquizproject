#multi_choice에 대한 url을 관리한다.
from django.urls import path, include
from .views import helloAPI, showQuiz, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("showQuiz/", showQuiz),
    path("randomQuiz/", randomQuiz),
    path("showQuiz/", showQuiz),
]