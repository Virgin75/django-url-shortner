from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Link(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, 
        on_delete=models.CASCADE)
    long_url = models.URLField(max_length=250)
    short_slug = models.SlugField(max_length=50, unique=True)
    nb_hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.long_url}, short is: {self.short_slug}"
