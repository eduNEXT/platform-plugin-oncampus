"""
URL configuration for the On Campus APIs.
"""

from django.urls import include, re_path

app_name = "platform_plugin_oncampus"

urlpatterns = [
    re_path(r'^api/', include("platform_plugin_oncampus.api.urls")),
]
