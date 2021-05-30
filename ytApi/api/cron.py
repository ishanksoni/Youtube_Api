from django_cron import CronJobBase, Schedule
from googleapiclient.discovery import build
import apiclient
from .models import *
from ytApi import settings
from datetime import datetime, timedelta


# Cron class to fetch videos as scheduled.
class CronJob(CronJobBase):

    RUN_EVERY_MINS = (10/ 60)  # 10 second

    schedule = Schedule(run_every_mins = RUN_EVERY_MINS)

    code = 'api.CronJob' # a unique code

    # Call Function
    def do(self):

        print("Test Passed")

        # Api Keys stored in envionment variable.
        apiKeys = settings.API_KEYS

        # Current Time
        currTime = datetime.now()

        print(currTime)

        latestTime = currTime - timedelta(minutes = 1)

        # To check if a valid API key exists or not in the apikeys.
        isValid = False

        for apiKey in apiKeys:

            print(apiKey, end= " <---")

            try:
                youtube = build("youtube", "v3", developerKey = apiKey)

                # Api call for vidoes.
                request = youtube.search().list(q = "cricket", part = "snippet", order="date", maxResults=50,
                                            publishedAfter = (latestTime.replace(microsecond=0).isoformat() + 'Z'))
                
                # Result.
                fetchedData = request.execute()

                # Api is valid
                isValid = True

            except apiclient.errors.HttpError as error:

                code = error.resp.status
                
                print("is in valid")

                if ((code == 400 or code == 403) ==  False):
                    break

            if (isValid == True):
                break

        # If Api key is valid.
        if isValid:

            print("API IS VALID ")

            for item in fetchedData['items']:
                videoId = item['id']['videoId']
                publishedTime = item['snippet']['publishedAt']
                title = item['snippet']['title']
                description = item['snippet']['description']
                channelId = item['snippet']['channelId']
                channelTitle = item['snippet']['channelTitle']

                # Create a tuple in Videos table with the fetchedData
                try:
                    Videos.objects.create(
                        videoId = videoId,
                        title = title,
                        description = description,
                        channelId = channelId,
                        channelTitle = channelTitle,
                        publishedTime = publishedTime,
                    )
                except error:
                    print(error)
                    

        else:
            print("NO valid Api key found")

