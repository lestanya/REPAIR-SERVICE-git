from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth import get_user_model
from .models import Request, Comment
from .forms import UserForm, RequestForm, CommentForm

User = get_user_model()


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']      # username из User
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.fio}!')
            return redirect('dashboard')
        messages.error(request, 'Неверный логин или пароль')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return redirect('index')


@login_required
def profile(request):
    user = request.user
    context = {
        'user_role': user.role,
        'user_phone': user.phone,
        'user_fio': user.fio,
    }
    return render(request, 'profile.html', context)


@login_required
def dashboard(request):
    # Фильтрация заявок по роли текущего пользователя
    user = request.user
    role = user.role

    if role == 'specialist':
        requests_qs = Request.objects.filter(master=user)
    elif role == 'client':
        requests_qs = Request.objects.filter(client=user)
    else:  # admin, manager, operator
        requests_qs = Request.objects.all()

    users = User.objects.all()
    comments = Comment.objects.all()

    # Инициализируем формы
    user_form = UserForm()
    request_form = RequestForm()
    comment_form = CommentForm()

    if request.method == 'POST':
        if 'user_submit' in request.POST:
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Пользователь добавлен!')
                return redirect('dashboard')

        elif 'request_submit' in request.POST:
            request_form = RequestForm(request.POST)
            if request_form.is_valid():
                request_form.save()
                messages.success(request, 'Заявка добавлена!')
                return redirect('dashboard')

        elif 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.save()
                messages.success(request, 'Комментарий добавлен!')
                return redirect('dashboard')

    context = {
        'users': users,
        'requests': requests_qs,
        'comments': comments,
        'user_form': user_form,
        'request_form': request_form,
        'comment_form': comment_form,
    }
    return render(request, 'dashboard.html', context)
