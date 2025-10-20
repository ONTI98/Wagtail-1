from django.db import models


from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class GenericPage(Page):
    banner_title=models.CharField(max_length=140,default="Welcome to my generic page")

    #extends content panels to include banner title
    content_panels=Page.content_panels+[
        FieldPanel("banner_title"),

    ]
