from django.contrib import admin
from django.urls import path, include
import snippets


urlpatterns = [
    path(r'^api-auth/', include('rest_framework_urls', namespace='rest_framework')),
    path(r'^', include('snippets.urls')),
]
