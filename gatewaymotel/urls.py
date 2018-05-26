from django.conf.urls import url
from . import views #.은 현재 폴더(elections)를 의미합니다.

app_name = 'gatewaymotel'

urlpatterns = [
    url(r'^$', views.index, name = 'home'), #위의 urls.py와는 달리 include가 없습니다.
    url(r'^index1/$', views.about, name = 'about'),
    url(r'^index2/$', views.attractions, name = 'attract'),
    url(r'^index3/$', views.room, name = 'room'),
    url(r'^index4/$', views.contact, name = 'contact'),
    ]
