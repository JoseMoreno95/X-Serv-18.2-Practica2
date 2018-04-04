from django.conf.urls import include, url
from django.contrib import admin
from acorta import views

urlpatterns = [
    url(r'^$', views.mainPage),
    url(r'^(\d+)/$', views.redirection),
    url(r'^admin/', include(admin.site.urls)),
]
