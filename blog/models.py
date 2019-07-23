from django.db import models

# Create a Blog model here.
# title
# pub_date
# body
# image

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()

# Add the Blog app to settings


# Create a migration


# Migrate


# Add to the Admin