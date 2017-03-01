"""yltek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from .serializers import UserSerializer, GroupSerializer
from main import views,rest_views
#from demo.views import HomePageView, DefaultFormView


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'customers', rest_views.CustViewSet)
router.register(r'groups', rest_views.GroupViewSet)
router.register(r'role', rest_views.RoleViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', views.login, name='login'),
    url(r'^test/$', views.test, name='test'),
    url(r'^demo/', include('demo.urls')),
    url(r'^erp/', include('erp.urls')),
    #url(r'^form$', DefaultFormView.as_view(), name='form_default'),
]
