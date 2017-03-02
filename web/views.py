from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm
# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('web:home'))
    else:
        template_path = 'web/login.html'
        return render(request, template_path)

@login_required
def home(request):
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_input = post_form.cleaned_data['post_field']
            current_user.post_set.create(post_text=post_input, time_stamp=timezone.now())
        return HttpResponseRedirect(reverse('web:home'))
    else:
        post_form = PostForm()
    posts = Post.objects.all()
    context = {
        'post_form' : post_form,
        'posts' : posts,
    }
    template_path = 'web/home.html'
    return render(request, template_path, context)
