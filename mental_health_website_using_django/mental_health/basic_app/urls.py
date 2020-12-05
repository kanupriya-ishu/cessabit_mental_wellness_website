from django.urls import path
from basic_app import views


# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('aboutUs/', views.about,name='about'),
    path('discuss/', views.discuss,name='discuss'),
    path('contact/', views.contact,name='contact'),
    path('discuss/', views.discuss,name='discuss'),
    path('articles/', views.articles, name='articles'),
    path('articles/kids', views.kidsarticle, name='kidsarticle'),
    path('articles/teenage', views.teenagearticle, name='teenagearticle'),
    path('articles/adult', views.adultarticle, name='adultarticle'),
    path('meditation/', views.meditation, name='meditation'),
    path('quiz/', views.quiz, name='quiz'),
]
