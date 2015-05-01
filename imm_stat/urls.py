from django.conf.urls import include, url
from django.contrib import admin
from imm_stat.views import profile, profile_update
from .views import IndexView, register

urlpatterns = [
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/update/$', profile_update, name='profile_update'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
