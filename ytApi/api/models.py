from typing import Tuple
from django.db import models

# Create your models here.

from django.db import models


# Video table class
class Videos(models.Model):

    # ID
    videoId = models.CharField(null = False, blank = False, max_length = 100)

    # Title
    title = models.CharField( null = True, blank = True, max_length = 100)

    # Discription
    description = models.CharField(null = True, blank = True, max_length = 1000)

    # Published Time
    publishedTime = models.DateTimeField()

    # Channel ID
    channelId = models.CharField(null = False, blank = False, max_length = 100)

    # Channel Title
    channelTitle = models.CharField(null = True, blank = True, max_length = 100)

    # Current Time in db.
    created = models.DateTimeField(null = True, blank = True, auto_now_add=True)