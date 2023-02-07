from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class Pagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
    page_query_param = 'page'

    def get_paginated_response(self, data):
        page_count = self.page.paginator.count // self.page_size
        if self.page.paginator.count % self.page_size != 0:
            page_count += 1

        return Response({
            'next': True if self.get_next_link() else False,
            'previous': True if self.get_previous_link() else False,
            'count': self.page.paginator.count,
            'pageCount': page_count,
            'results': data
        })
