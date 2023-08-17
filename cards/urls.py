from django.urls import path

from .views import StartQuizView, CardView, AddQuestion


app_name = "cards"
urlpatterns = [
    path("", StartQuizView.as_view(), name="start_quiz"),
    path("card/", CardView.as_view(), name="card"),
    path("add/", AddQuestion.as_view(), name="add"),
]