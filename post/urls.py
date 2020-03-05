
from django.urls import path, re_path
from django.conf.urls import url   # sonradan import ettim. django 3 ile sanıtım artık path kullanılıyor. araştır.
from .views import *

app_name = 'post'       # aşağıdaki url name leri başka app lar ile karışmasın diye model dosyasında uygulamaadı.urladı şeklinde kullanılır.

urlpatterns = [
    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detay'),       # önemli djnago 3 için url de kullanılacak regular exception araştır.
    re_path(r'^(?P<slug>[\w-]+)/update/$', post_update, name='guncelle'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='sil'),
    #url(r'^$', home_view)
]
