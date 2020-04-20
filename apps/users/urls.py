from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^new', views.new),

    url(r'^signin', views.signin),

    url(r'^register', views.register),

    url(r'^edit', views.edit),

    url(r'^dashboard', views.dashboard),
]

# urlpatterns = [
#     url(r'^users/new', views.new),
# ]