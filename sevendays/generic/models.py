from django.db import models


from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

class GenericPage(Page):
    banner_title=models.CharField(max_length=140,default="Welcome to my generic page")
    introduction=models.TextField(max_length=140)
    banner_image=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',   
    )
    author=models.ForeignKey(
        'Author' , #this will point to the author class below, for that we use a string
         null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+', 
    )
    #extends content panels to include banner title
    content_panels=Page.content_panels+[
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),

    ]

@register_snippet
class Author(models.Model):
    name=models.CharField(max_length=140,blank=True,)
    title=models.CharField(max_length=140,blank=True,)
    company_name=models.CharField(max_length=140,blank=True,)
    company_url=models.URLField(blank=True)
    image=models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )

   

    panels=[
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("company_name"),
        FieldPanel("company_url"),
        FieldPanel("image")
    ] 
    
    def __str__(self):
        return self.name