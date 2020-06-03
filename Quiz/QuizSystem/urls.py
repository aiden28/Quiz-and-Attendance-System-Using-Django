from django.urls import path
from QuizSystem import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('contactUs/',views.contactUs,name='contactUs'),

]