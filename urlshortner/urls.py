from django.urls import path
from .views import RedirectToLinkView
 
urlpatterns = [
    path('<slug:url_slug>', RedirectToLinkView.as_view()),
]