
from django.urls import path, re_path
from django.conf.urls import url   # sonradan import ettim. django 3 ile sanıtım artık path kullanılıyor. araştır.
from .views import *

app_name = 'accounts'       # aşağıdaki url name leri başka app lar ile karışmasın diye model dosyasında uygulamaadı.urladı şeklinde kullanılır.

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
