from django.shortcuts   import render, get_object_or_404, redirect
from django.utils       import timezone
from .models            import Post
from .forms             import BlogPostForm

def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/blogposts.html", {'posts': posts})

def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/postdetail.html", {'post': post})

def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    
    The first line (post = ...) if to take already existing post, 
    to edit it and showing all the data for that post.
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    
    if request.method == "POST":
        
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            
            post        = form.save(commit=False)
            """
            To keep the same author if the admin want to edit,
            if no author ==> first creation, take the user as author
            if author    ==> we keep it (no action on it)
            """
            if not post.author : 
                post.author = request.user
            post.save()
            
            return redirect('post_detail', post.pk)
    
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'posts/blogpostform.html', {'form': form})