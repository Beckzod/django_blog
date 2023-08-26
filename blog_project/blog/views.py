from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView


# def bloglistview(request):
#     blogs = Blog.objects.all()

#     context = {
#         'blogs': blogs
#     }

#     return render(request, 'home.html', context=context)


# def blogdetailview(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     context = {
#         'blog': blog
#     }
#     return render(request, 'blogdetail.html', context=context)

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogdetail.html'
    context_object_name = 'blog'
