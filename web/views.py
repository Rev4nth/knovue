from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import  timezone
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.postgres.search import SearchVector

from taggit.models import Tag

from .models import Post
from .forms import PostForm
# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('web:post_list'))
    else:
        template_path = 'web/login.html'
        return render(request, template_path)

@login_required
def post_list(request, tag_slug=None):
    current_user = request.user
    posts = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_title = post_form.cleaned_data['post_title']
            post_input = post_form.cleaned_data['post_field']
            post_tags = post_form.cleaned_data['post_tags']
            post_image = post_form.cleaned_data['post_image']
            post = current_user.post_set.create(title=post_title, 
                    text=post_input, image=post_image, created=timezone.now())
            post.tags.add(*post_tags)
        return HttpResponseRedirect(reverse('web:post_list'))
    else:
        post_form = PostForm()
    context = {
        'post_form' : post_form,
        'posts' : posts,
        'tag' : tag,
    }
    template_path = 'web/home.html'
    return render(request, template_path, context)

@login_required
def like(request):
    if request.method == 'POST':
        user = request.user
        post_id = int(request.POST.get('id'))
        post = Post.objects.get(pk=post_id)
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)
    likes_count = post.total_likes()
    is_liked = post.likes.filter(id=user.id).exists()
    context = {
        'likes_count' : likes_count,
        'is_liked' : is_liked,
    }
    return JsonResponse(context)

@login_required
def profile(request):
    current_user =  request.user
    social_user = request.user.social_auth.filter(provider='facebook').get(user=request.user)
    facebookId = social_user.uid
    facebook_image_url= 'http://graph.facebook.com/' + facebookId +'/picture?width=120&height=120'
    posts = Post.objects.filter(user_id=current_user.id)
    context = {
        'facebook_image_url' : facebook_image_url,
        'posts' : posts,
    }
    template_path = 'web/profile.html'
    return render(request, template_path, context)

@login_required
def post_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('web:profile'))

@login_required
def search(request):
    query = request.GET['q']
    title_vector = SearchVector('title')
    text_vector = SearchVector('text')
    res = Post.objects.annotate(search=title_vector
            +text_vector).filter(search=query)
    context = {
        'search_posts' : res,
    }
    template_path = 'web/search.html'
    return render(request, template_path, context)

