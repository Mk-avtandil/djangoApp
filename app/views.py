from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Marvel
from .forms import PostForm


class Home(ListView):
    template_name = 'app/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Marvel.objects.all()
        else:
            if Marvel.objects.count() < 3:
                return Marvel.objects.all()
            return Marvel.objects.order_by('?')[:3]


class DetailPost(DetailView):
    model = Marvel
    template_name = 'app/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Marvel.objects.filter(slug=self.kwargs['slug'])


class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'app/create_post.html'
    success_url = reverse_lazy('home')

