from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from .pagination import *


class ResultsPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoList(generics.ListAPIView):

    queryset = Videos.objects.all().order_by('-publishedTime')

    serializer_class = VideosSerializer
    pagination_class = ResultsPagination 
