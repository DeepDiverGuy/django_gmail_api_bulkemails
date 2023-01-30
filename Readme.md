### GMAIL API implementation for sending bulk emails


# Prerequisites

- A Google Workspace Account
- Go to https://developers.google.com/gmail/api/quickstart/python & follow the instructions properly


# Dependencies

```
pip install django
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install dotenv # if needed

```

# What you need to do


- clone this reppository

- Set up a virtual environment
```
python -m venv virenv-gmailapi

```

- activate it
```
source virenv-gmailapi/bin/activate # for linux

```

- from the project's base directory
```
python manage.py runserver

```

- enjoy!