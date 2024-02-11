from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


class ConflictError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _("Resource already exists.")
    default_code = "conflict"

    def __init__(self, method, detail=None, code=None):
        if detail is None:
            detail = force_str(self.default_detail).format(method=method)
        super().__init__(detail, code)
