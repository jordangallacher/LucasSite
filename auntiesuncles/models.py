from django.db import models

# Create a Blog model here.
# title
# pub_date
# body
# image

class Auntiesuncles(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title    # This function names the posts in the admin panel

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# Add the Blog app to settings

# Create a migration

# Migrate

# Add to the Admin
