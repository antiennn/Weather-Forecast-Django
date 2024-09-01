from django.db import models


class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField()
    query = models.TextField()
