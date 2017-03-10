from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect

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
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_input = post_form.cleaned_data['post_field']
            post_tags = post_form.cleaned_data['post_tags']
            post = current_user.post_set.create(post_text=post_input, created=timezone.now())
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
