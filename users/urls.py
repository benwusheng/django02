from django.conf.urls import url

import users
from users import views

urlpatterns = [
    url(r"^index/$",views.index),
    url(r"^news/(?P<category>\d+)/(?P<page>\d+)$", users.views.news),
    url(r"news2$",views.news2)
]