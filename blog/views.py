from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.utils import timezone
from blog.forms import  CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#@login_required
def blog_view(request):  
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now())   
    #return render (request , 'blog/blog-home.html',context)
    paginator = Paginator(posts, 2) # 3 پست در هر صفحه
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts':posts,'page_obj': page_obj}
    return render(request , 'blog/blog-home.html', context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks . Your message has been received.')
    
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    if not post.login_require:
        comment = Comment.objects.filter(approach=True,post=post.id).order_by('created_date')
        post.counted_views +=1
        post.save()
        form = CommentForm()
        content = {'post':post,'comment':comment,'form':form}
        return render(request,'blog/blog-single.html',content)
    else:
        return redirect('accounts:login')
