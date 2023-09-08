from rest_framework.views import APIView
from rest_framework.response import Response


from django.core.exceptions import (  # lint-amnesty, pylint: disable=wrong-import-order
    ObjectDoesNotExist,
    ValidationError
)

from openedx.core.lib.api.permissions import ApiKeyHeaderPermissionIsAuthenticated
from openedx.core.djangoapps.enrollments.views import CourseEnrollmentsApiListView
from openedx.core.djangoapps.enrollments.forms import CourseEnrollmentsApiListForm
from common.djangoapps.student.models import CourseEnrollment

class UserCourseEnrollmentsListAPI(CourseEnrollmentsApiListView):

    permission_classes = (ApiKeyHeaderPermissionIsAuthenticated,)

    def get_queryset(self):
        """
        Get all the course enrollments for the given course_id and/or given list of usernames.
        """
        form = CourseEnrollmentsApiListForm(self.request.query_params)

        if not form.is_valid():
            raise ValidationError(form.errors)

        queryset = CourseEnrollment.objects.all()
        course_id = form.cleaned_data.get('course_id')
        email = self.request.query_params.get('email')

        if course_id:
            queryset = queryset.filter(course_id=course_id)
        if email:
            queryset = queryset.filter(user__email__startswith=email)

        return queryset
