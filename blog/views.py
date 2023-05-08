from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes, AboutUs
from .form import CommentsFrom


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class AboutUsView(View):
    def get(self, request):
        aboutus = AboutUs.objects.all()
        return render(request, 'blog/about.html', {'persons': aboutus})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComents(View):
    def post(self, request, pk):
        form = CommentsFrom(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def Get_client_IP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = Get_client_IP(request)
        print(f'call ip:{ip_client} {pk}')
        like = Likes.objects.filter(ip=ip_client, pos_id=pk)
        if like.exists():
            like.delete()
        else:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
        return redirect(f'/{pk}')
