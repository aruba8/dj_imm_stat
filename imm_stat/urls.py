from django.conf.urls import include, url
from django.contrib import admin
from imm_stat.views import profile, profile_update
from .views import index_view, register, statistic_view, edit_federal_statistic_view, edit_provincial_statistic_view

urlpatterns = [
    # Examples:
    url(r'^$', index_view, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^profile/$', profile, name='profile'),
    url(r'^statistic/(?P<pk>[0-9]+)/$', statistic_view, name='statistic'),
    url(r'^stat/update/fed$', edit_federal_statistic_view, name='edit_federal_statistic'),
    url(r'^stat/update/prov$', edit_provincial_statistic_view, name='edit_provincial_statistic'),
    url(r'^profile/update/$', profile_update, name='profile_update'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
