import rest_framework_simplejwt.views
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django_rq import get_queue
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .forms import CreateUsersForm
from django.contrib.auth import authenticate


def say_hello():
    return 'Hello'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['id'] = self.user.id
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def start(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('tasks', request.POST['id'], request.POST['token_refresh'], request.POST['token_access'])
    else:
        return redirect('login')


def tasks(request, id, token_refresh, token_access):
    context = {
        'token_refresh': token_refresh,
        'token_access': token_access,
        'id': id,
    }
    return render(request, 'todoApp/task.html', context)


def register(request):
    form = CreateUsersForm()
    if request.method == 'POST':
        form = CreateUsersForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'todoApp/register.html', context)


def log(request):
    if request.method == 'POST':
        messages.success(request, 'Disconnected.')
        logout(request)
    return render(request, 'todoApp/login.html', context={})


def success(request):
    queue = get_queue()
    queue.enqueue(say_hello)
    return render(request, 'django_rq/test.html',{})

def error(request):
    queue = get_queue()
    queue.enqueue(say_hello)
    raise ValueError

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
