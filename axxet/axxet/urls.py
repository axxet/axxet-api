from django.conf.urls import patterns, include, url
from django.contrib import admin

from axxet.apps.router_v1 import router

# Admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns += patterns('',
  url(r'^api/', include(router.urls)),
  url(r'^api/token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
