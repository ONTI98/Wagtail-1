from django.db import models

from wagtail.models import Page


class HomePage(Page):
    banner_title=models.CharField(max_length=140,default="Welcome to my home wagtail")


