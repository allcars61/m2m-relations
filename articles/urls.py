# from django.urls import path
#
# from articles.views import articles_list
#
# urlpatterns = [
#     path('', articles_list, name='articles'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
]
