from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #아무것도 뒤에 안 붙으면 views에서 처리
    path('some_url', views.some_url)
]
