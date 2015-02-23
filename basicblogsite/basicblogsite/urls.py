from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'basicblogsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blogsite/', include('blogsite.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
