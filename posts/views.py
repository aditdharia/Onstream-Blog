from django.shortcuts import render,get_object_or_404,redirect
from .forms import postForm
from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def post_create(request):
    form=postForm(request.POST or None)
    if form.is_valid():
       instance=form.save(commit=False)
       instance.save()
    context={
        "form":form,
    }
    return render(request,"post_form.html",context)


def post_detail(request,id):
    instance=get_object_or_404(Post,id=id)
    context={
        "instance":instance
    }
    return render(request,"post_detail.html",context)



     

def post_list(request):
    query_set_list=Post.objects.all().order_by("-timestamp")
    query_list=request.GET.get('query')
    if query_list:
        query_set_list=query_set_list.filter(Q(title__icontains=query_list)| Q(content__icontains=query_list)).distinct()
    paginator = Paginator(query_set_list,4)

    page = request.GET.get('page')
    query_set = paginator.get_page(page)
    context={
        "object_list":query_set
    }
    return render(request,"index.html",context)


def delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    instance.delete()
    return redirect("post:list")