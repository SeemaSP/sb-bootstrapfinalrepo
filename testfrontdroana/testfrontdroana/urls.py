"""testfrontdroana URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from testfrontdroana.views import start, dashboard, charts, tables, \
     forms, bootstrap_elements, bootstrap_grid, rtl_dashboard, blank
    

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^$', start, name='sb_admin_start'),
        url(r'^dashboard/$', dashboard, name='sb_admin_dashboard'),
        url(r'^charts/$', charts, name='sb_admin_charts'),
        url(r'^tables/$', tables, name='sb_admin_tables'),
        url(r'^forms/$', forms, name='sb_admin_forms'),
        url(r'^bootstrap-elements/$', bootstrap_elements, name='sb_admin_bootstrap_elements'),
        url(r'^bootstrap-grid/$', bootstrap_grid, name='sb_admin_bootstrap_grid'),
        url(r'^rtl-dashboard/$', rtl_dashboard, name='sb_admin_rtl_dashboard'),
        url(r'^blank/$', blank, name='sb_admin_blank'),
        url(r'^admin/', admin.site.urls),        
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ##    url(r'^accounts/login/$', auth_views.login,
        ##    {'template_name': 'django_sb_admin/examples/login.html'}),
        ]
