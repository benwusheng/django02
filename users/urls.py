from django.conf.urls import url

import users
from users import views

urlpatterns = [
    url(r"^index/$",views.index),
    url(r"^news/(?P<category>\d+)/(?P<page>\d+)$", users.views.news),
    url(r"news2$",views.news2),
    url(r"news3$",views.news3),
    url(r"news4$",views.news4),
    url(r"resp$",views.resp),
    url(r"^index$",views.index,name="index"),
    url(r"^set_cookie$",views.set_cookie),
    url(r"^get_cookie$",views.get_cookie),
    url(r"^get_session",views.get_session),
    url(r"set_session",views.set_session),
    url(r"del_session",views.del_session),
    # url(r"^post$",views.post),
    # url(r"^do_post$",views.do_post),
    url(r"^the_post$",views.the_post),
    url(r"^post2$",views.PostView.as_view())
]