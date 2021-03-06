from django.contrib.auth import login
from django.forms.fields import NullBooleanField
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Link
from .forms import LinkForm
from .utils import generate_unique_slug

class RedirectToLinkView(View):

    def get(self, request, url_slug):

        # Get redirection link
        link_obj = get_object_or_404(Link, short_slug=url_slug)
        redirect_to = link_obj.long_url
        
        # Counting the number of redirects
        link_obj.nb_hits += 1
        link_obj.save()

        return HttpResponseRedirect(redirect_to)

class ShortenLinkView(View):

    def get(self, request):
        form = LinkForm()
        return render(request, "urlshortner/index.html", {'form': form})

    def post(self, request):

        def get_user():
            if request.user.is_anonymous:
                return None
            else:
                return request.user

        # create a form instance and populate it with data from the request:
        form = LinkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            shortened_url = Link(
                owner=get_user(),
                long_url= form.cleaned_data['long_url'],
                short_slug= generate_unique_slug()
            )
            shortened_url.save()
            return render(
                request, "urlshortner/link-created.html",
                {
                    'shorten_link': shortened_url.short_slug,
                    'domain': request.build_absolute_uri('/')[:-1]
                }
            )

class MyLinksView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        my_links = Link.objects.filter(owner=user)

        return render(
            request, "urlshortner/my-links.html",
            {
                'my_links': my_links,
                'domain': request.build_absolute_uri('/')[:-1]
            }
        )
