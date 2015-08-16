"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register$', views.register, name='users-register'),
    url(r'^limited', views.limited, name='limited'),
    url(r'^email/confirm/(?P<code>.+)', views.confirm_email, name='confirm-email'),
    url(r'^email/confirmation',
        TemplateView.as_view(template_name='users/confirmation-email-sent.html'),
        name='confirmation-sent'),
    url(r'^email/send-confirmation', views.send_email_confirmation, name='send_email_confirmation'),
]
