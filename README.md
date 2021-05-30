# Youtube_Api
An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

### Feature Implemented.
    1. Cron job fetch recent videos on topic - 'cricket' and populates db on every 10 sec.
    2. rest api for chronological reverse sorted according to publishing date-time in page number pagination.
    3. Search Option uses defalut drf Search query to search by 'title' (keyword).
    4. Filter Option uses django backend filter for filter query api.

## Development 🔧

## Setup

```sh
$ git clone https://github.com/ishanksoni/Youtube_Api.git
$ cd Youtube_Api
```

### For setting virtual environment

```sh
$ virtualenv venv
```

### For activating virtual environment in Windows

```sh
$ venv/Scripts/activate
```

After creating virtual environment

### Start

```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```

    Write all available API Keys in apiKeys.txt file  

Setup crontab to run CronJob, refer [this](https://django-cron.readthedocs.io/en/latest/installation.html)

### Run server

```sh
python mange.py runserver
```

### See Api visualisation by generic api view.
    open http://127.0.0.1:8000/ 
