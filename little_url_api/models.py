from django.db import models


class Url(models.Model):
    long = models.CharField(max_length=255)
    short = models.CharField(max_length=255)
