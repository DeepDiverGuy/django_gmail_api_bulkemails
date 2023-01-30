"""
Function: Using Google's GmailAPI, I am sending test-emails in BULK to the email address' provided. I have used Django's development server.

Source: Search for "gmail api python quickstart" & go to the official doc.

Requirements (Follow the Source):
- Account: Google Workspace Account
- Project: A Google Cloud Project
- Authentication for Google Services: 
    - OAuth2.0 [a 'Service Account' can be used instead, tht's more professional]
    - The credentials.json file needs to be downloaded & the path to be pointed to from the app.
- Scope: https://mail.google.com/

"""


import re
import os
import time

# from django.shortcuts import render
from .forms import emails_form
from django.views.generic.edit import FormView
from django.contrib import messages
# from django.http import HttpResponseRedirect

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
import base64
from email.message import EmailMessage

from dotenv import load_dotenv
load_dotenv()



'''
If scopes are modified, delete the file "credentials-oauth2.json"
'''
SCOPES = [os.environ['GMAIL_SCOPE']] # The scopes (APIs) you have to use in this app.
OAuth2_credentials_json_file = os.environ['OAuth2_credentials_json_file'] # The path where the file is. you have to download this file from the Google Cloud Project
Workspace_Account = os.environ['Workspace_Account'] # the email id which is registered as a Google Workspace Account
 

class handle_email_form(FormView):

    template_name = 'emailsendingapp/emails_form.html'
    form_class = emails_form
    success_url = '/emailsend/'
    extra_context = {}


    def form_valid(self, form):

        success_emails = []
        failed_emails = []

        text = form.cleaned_data['emails']
        extracted_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        # print(extracted_emails)

        i = 0 
        
        for email in extracted_emails:

            '''
            gmail api's "message.send" has limits.
            100 emails per second per user.
            '''
            i+=1
            if i%90 == 0:
                time.sleep(1)


            creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(OAuth2_credentials_json_file, SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json()) # It's gonna be written in the base directory of this django project

            try:
                # Calling the Gmail API
                service = build('gmail', 'v1', credentials=creds)
                
                message = EmailMessage()
                message['From'] = Workspace_Account # corresponding workspace account (maybe)
                message['Subject'] = 'Test Email'
                message.set_content('This is an automated test mail from Sagor, the Developer. Your test OTP is 1234')
                message['To'] = email # each email from submitted emails from the html form

                # encode the message
                encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

                create_message = {
                    'raw': encoded_message
                }
                # pylint: disable=E1101
                service.users().messages().send(userId="me", body=create_message).execute()
                # print(F'Message Id: {send_message["id"]}')
                
                '''
                NOTE: I need to set-up a logic (raise Exception) here, in case the message didn't get sent & no error occurs [using return value of the API]. To append that email to the failed list. But that's for later, I got works to do now.
                '''
                success_emails.append(email)
            
            except Exception:
                failed_emails.append(email)
                # print(success_emails)


        self.extra_context['success_emails'] = success_emails 
        self.extra_context['failed_emails'] = failed_emails

        messages.success(self.request, 'Operation done')
        return super().form_valid(form)



