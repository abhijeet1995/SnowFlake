from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from my_music import views

urlpatterns = [
    url(r'^', views.index, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^my_music', include('my_music/urls')),
]
