from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from article.models import Post
from article.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

################################
##      Class Based Views     ##
################################
from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'article/about.html')

class PostListView(ListView):
    #if no template name is said here. The default one is post_list.html. It is just
    # the first and second words lower cased and with an underscore
    model = Post

    # Define how I want to grab this list
    def get_queryset(self):
        # This allow us to deal with django ORMs (Object-related models)
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
                                    # lte = Less Than or Equal to
                                    # for more info on it, look for "Field Lookups on django documentation:
                                    # https://docs.djangoproject.com/en/1.10/topics/db/queries/#field-lookups

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/' # if this person is not logged in, where should this person go? To login_url
    redirect_field_name = 'article/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/' # if this person is not logged in, where should this person go? To login_url
    redirect_field_name = 'article/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('article:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'article/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


################################
##        Function Views      ##
################################


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('article:post_detail', pk=pk)
