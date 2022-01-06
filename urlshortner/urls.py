from django.urls import path
from .views import RedirectToLinkView, ShortenLinkView, MyLinksView
 
urlpatterns = [
    path('', ShortenLinkView.as_view(), 
        name="shortenlinkview"),
    path('my-links', MyLinksView.as_view(), 
        name="mylinksview"),
    path('<slug:url_slug>', RedirectToLinkView.as_view()),
]