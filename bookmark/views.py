from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

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


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['name', 'url']  # '__all__'
    template_name_suffix = '_update'  # bookmark_update.html
    # success_url = reverse_lazy('bookmark:list')
    # success_url이 없으면 기본적으로 model의 get_absolute_url() 함수를 호출
