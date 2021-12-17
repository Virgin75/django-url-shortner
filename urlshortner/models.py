from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Link(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    long_url = models.URLField(max_length=250)
    short_slug = models.SlugField(max_length=50)
    nb_hits = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.long_url}, short is: {self.short_slug}"
