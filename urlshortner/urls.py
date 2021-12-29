from django.urls import path
from .views import RedirectToLinkView, ShortenLinkView
 
urlpatterns = [
    path('shorten', ShortenLinkView.as_view(), 
        name="shortenlinkview"),
    path('goto/<slug:url_slug>', RedirectToLinkView.as_view()),
]