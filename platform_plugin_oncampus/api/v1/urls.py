"""

"""

from django.conf.urls import url

from platform_plugin_oncampus.api.v1 import views

urlpatterns = [
    url(r'^user/enrollments/$', views.UserCourseEnrollmentsListAPI.as_view(), name="user-enrollment"),
]
