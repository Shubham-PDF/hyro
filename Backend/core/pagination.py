from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# class JobPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = "page_size"
#     max_page_size = 100

class JobPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            "success": True,
            "message": "Jobs fetched successfully",
            "current_page": self.page.number,
            "total_pages": self.page.paginator.num_pages,
            "total_results": self.page.paginator.count,
            "results": data
        })
