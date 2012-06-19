from wikicamp.wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
import markdown
import htmllib
from django.template import RequestContext, loader
from django.core.context_processors import csrf
# Create your views here.

def view_page(request, page_name):
    c = {}
    try:
     page = Page.objects.get(pk=page_name)
     content = page.content
    except Page.DoesNotExist:
        return render_to_response("create.html", {"page_name":page_name}, context_instance=RequestContext(request))
        content = page.content
        return render_to_response("view.html", {"page_name":page_name, "content":content}, context_instance=RequestContext(request))

def edit_page(request, page_name):
    c = {}
    try:
     page = Page.objects.get(pk=page_name)
     content = page.content
    except Page.DoesNotExist:
     content = ""
    return render_to_response("edit.html", {"page_name":page_name, "content":content}, context_instance=RequestContext(request))
    print()

def save_page(request, page_name):
    c = {}
#     content = request.POST['content', 'this is the default']
    try:
     page = Page.objects.get(pk=page_name)
     content = request.GET['content']
     page.content = 'content'
#    except Page.DoesNotExist:
     Page = Page(name=page_name, page_content=content)
#     page.save()
#    return HttpResponseRedirect ("wikicamp/" + "{{page_name}}" + "/")
#    return HttpResponseRedirect("wikicamp/" + page_name + "/)
