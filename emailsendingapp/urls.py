from django.urls import path, include
from. import views


urlpatterns = [
    path('', views.handle_email_form.as_view(), name='handle_email_form'),
]


