from typing import Tuple
from django.db import models

# Create your models here.

from django.db import models


# Video table class
class Videos(models.Model):
    # ID
    videoId = models.CharField(null = False, blank = False, max_length = 100)

    # Title
    title = models.CharField( null = True, blank = True, max_length = 1000)

    # Discription
    description = models.CharField(null = True, blank = True, max_length = 5000)

    # Published Time
    publishedTime = models.DateTimeField()

    # Channel ID
    channelId = models.CharField(null = False, blank = False, max_length = 100)

    # Channel Title
    channelTitle = models.CharField(null = True, blank = True, max_length = 100)