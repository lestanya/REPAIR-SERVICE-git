from django.shortcuts import render
from .models import User, Request, Comment
from .forms import UserForm, RequestForm, CommentForm

def dashboard(request):
    users = User.objects.all()
    requests = Request.objects.all()
    comments = Comment.objects.all()
    
    user_form = UserForm()
    request_form = RequestForm()
    comment_form = CommentForm()
    
    context = {
        'users': users, 'requests': requests, 'comments': comments,
        'user_form': user_form, 'request_form': request_form, 'comment_form': comment_form,
    }
    return render(request, 'dashboard.html', context)

