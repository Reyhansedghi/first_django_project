from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView
from django.views.generic import TemplateView

# Create your views here.
class DashBoard(TemplateView):
    template_name='cadmin/index.html'
    
class PostList(LoginRequiredMixin,ListView):
    model=Post
    template_name='cadmin/data.html'
    context_object_name='posts'

class CreatPost(LoginRequiredMixin,CreateView):
    model=Post
    #template_name='cadmin/data.html'