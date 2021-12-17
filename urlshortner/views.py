from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Link

class RedirectToLinkView(View):

    def get(self, request, url_slug):

        # Get redirection link
        link_obj = get_object_or_404(Link, short_slug=url_slug)
        redirect_to = link_obj.long_url

        # Counting the number of redirects
        link_obj.nb_hits += 1
        link_obj.save()

        return HttpResponse(link_obj.nb_hits)
        #return HttpResponseRedirect(redirect_to)
