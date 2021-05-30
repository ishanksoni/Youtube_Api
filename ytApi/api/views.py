from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .pagination import *


# View Function for the rest_api call of video list.
class VideoList(generics.ListAPIView):
    searchFields = ['title']
    filterBackends = (filters.SearchFilter, DjangoFilterBackend ,filters.OrderingFilter)
    filterset_fields = ['channelTitle']

    defaaultOrdering = ('-publishedTime')

    # Query set for data in db.
    queryset = Videos.objects.all()

    # Serialize class.
    serializer_class = VideosSerializer

    # Pagination
    pagination_class = VideoListPagination