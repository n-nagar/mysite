from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
	url(r'^$', views.index, name='Index'),
	url(r'^index2$', views.index2, name='Index2'),
	url(r'^storeauthcode$', csrf_exempt(views.storeauthcode), name='storeauthcode'),
]
