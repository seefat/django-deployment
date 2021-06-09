from django.conf.urls import url
from django.urls import path
from third_app import views

app_name = 'third_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
]
