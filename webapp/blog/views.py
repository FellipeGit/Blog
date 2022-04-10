from django.views import generic
from blog.models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'

class PostContent(generic.DetailView):
    model = Post
    template_name = 'post_content.html'

