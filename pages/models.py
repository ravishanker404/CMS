from django.db import models

class MultiPage(models.Model):
    page_name = models.CharField(max_length=255)
    entered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)

class MultiPageContent(models.Model):
    multi_page = models.ForeignKey(MultiPage)
    title = models.CharField(max_length=300)
    meta_keywords = models.CharField(max_length=300)
    content = models.TextField()
    updated_date = models.DateTimeField(auto_now = True)

class StaticPage(models.Model):
    page_name = models.CharField(max_length=255)
    title = models.CharField(max_length=300)
    meta_keywords = models.CharField(max_length=300)
    content = models.TextField()
    entered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)