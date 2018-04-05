from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$', views.index, name='landing'),
    url(r'^profile/',views.profile,name = 'profile'),
]
