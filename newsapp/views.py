from django.shortcuts import render, redirect
from django.views.generic.base import View

from .form import CommentsForm
from .models import News, Likes


class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        return render(request, 'news/news.html', {'news_list': news})


class NewsDetail(View):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        return render(request, 'news/news_detail.html', {'news': news})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.news_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request,):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, news_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.news_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
