from django.contrib import admin
from django.urls import path
from django.urls import re_path
from kokurcho_app import views

urlpatterns = [
    path('', views.main_menu),

    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    re_path(r'^form_telegram', views.form_telegram),
    re_path(r'^main_menu', views.main_menu),
    re_path(r'^valid', views.valid),
    re_path(r'^feedback', views.feedback),
    path('admin/', admin.site.urls),
    path('create_comment/', views.create_comment),
    path('get_comment/', views.get_comment),
]
