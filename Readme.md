# GMAIL API implementation for sending bulk emails with DJANGO


## Technical Information (Unfinished)

## Prerequisites (Unfinished)

- A Google Workspace Account
- Go to https://developers.google.com/gmail/api/quickstart/python & follow the instructions properly


## Dependencies

```
pip install django
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install dotenv # if needed
```

## What you need to do


- Clone this reppository

- Set up a virtual environment
```
python -m venv virenv-gmailapi
```

- Activate it
```
source virenv-gmailapi/bin/activate # for linux
```

- From the project's base directory
```
python manage.py runserver
```

- Go to http://localhost:8000/emailsend

- Submit all the emails in the form. No specific format is needed. The program will automatically detect the emails only & start sending.

- Enjoy!

## Issues

I didn't have enough time to test every aspect of this project. So, issues can occur. Please open one when you encounter.
