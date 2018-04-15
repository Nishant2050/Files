from django.conf.urls import url, include
from django.contrib import admin
from video import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.IndexView, name='index'),
    url(r'^upload/$', views.UploadFiles, name='upload'),
    # url(r'^display/$', views.DisplayFiles, name='display')
]