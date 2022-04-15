from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    # bookmark_list.html, {'bookmark_list':Bookmark.objects.all()}


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']  # '__all__'
    # 지정 안해주면 bookmark_form.html 그대로 사용
    template_name_suffix = '_create'  # bookmark_form.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')

