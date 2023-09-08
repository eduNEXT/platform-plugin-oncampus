"""
URL module for On Campos plugin API.
"""
from django.urls import include, re_path

app_name = "platform_plugin_oncampus"

urlpatterns = [
    re_path(r'v1/', include("platform_plugin_oncampus.api.v1.urls")),
]
