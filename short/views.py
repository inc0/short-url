# -*- coding: utf-8 -*-
from forms import UrlForm
from models import Url
from django.shortcuts import render_to_response, get_object_or_404
from  django.template import RequestContext
from django.http import HttpResponseRedirect
import utils

def main(request, **kwargs):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = Url()
            url.original_url = form.cleaned_data['url']
            url.save()
            c = {
                 "form": form,
                 "url": url,
                 }
            return render_to_response("main.html", c, context_instance=RequestContext(request))
        else:
            c = {
                 "form": form,
                 }
            return render_to_response("main.html", c, context_instance=RequestContext(request))
    else:
        form = UrlForm()
        c = {
                 "form": form,
                 }
        return render_to_response("main.html", c, context_instance=RequestContext(request))

def redirect_to_original(request, suffix, **kwargs):
    url = get_object_or_404(Url, suffix=suffix)
    
    return HttpResponseRedirect(url.original_url)