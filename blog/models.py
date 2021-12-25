from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    lead = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    description = models.CharField(null=True, blank=True, max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "blog_id:" + str(self.id) + "," + self.title + "...(" + str(self.updated_datetime) + ")"