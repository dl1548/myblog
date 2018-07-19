# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

from django.http import HttpResponse

from blog.models import Article

from datetime import datetime

def detail(request, id):
    #post = Article.objects.all()[int(my_args)]
    try:
        detail = Article.objects.get(id=int(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'detail' : detail})

def index(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 7) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'index.html', {'post_list' : post_list})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

def category(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'category.html', {'post_list' : post_list})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'index.html')
        else:
            post_list = Article.objects.filter(Q(content__icontains = s) | Q(title__icontains = s))
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,'error' : False})
    return redirect('/')