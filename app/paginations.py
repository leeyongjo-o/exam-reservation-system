from collections import OrderedDict

from django.conf import settings
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginator(Paginator):
    """object_list를 QuerySet이 아닌 list로 변환해두어 여러번 요청하지 않고 데이터 처리"""

    def __init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True):
        super().__init__(list(object_list), per_page, orphans, allow_empty_first_page)


class DefaultPagination(PageNumberPagination):
    page_size = settings.REST_FRAMEWORK.get('PAGE_SIZE', 10)
    page_query_description = '페이지 번호'
    page_size_query_description = '페이지당 반환할 결과 수'

    page_size_query_param = 'page_size'
    django_paginator_class = CustomPaginator

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('results', data),
        ]))

    def get_paginated_response_schema(self, schema):
        result = super().get_paginated_response_schema(schema)
        del result['properties']['next']
        del result['properties']['previous']
        return result
