import logging

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # 예상치 못한 오류 발생 대비
    if response is None:
        api_exception = APIException("오류가 발생하였습니다.")
        api_exception.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response = Response({'detail': api_exception.detail}, status=api_exception.status_code)

    # 오류 로깅
    if response.status_code >= 500:
        logging.exception(response.data)
    else:
        logging.warning(response.data)
    return response
