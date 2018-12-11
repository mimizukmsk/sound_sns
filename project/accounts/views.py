import logging

# from django.conf import setting
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views import View

from .forms import LoginForm, RegisterForm, ProfileForm

logger = logging.getLogger(__name__)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        # ログイン済の場合タイムライン画面へリダイレクト
        if request.user.is_authenticated:
            return redirect(reverse('timeline:index'))

        context = {
            'form': RegisterForm(),
        }
        return render(request, 'accounts/register.html', context)

    # def post(self, request, *args, **kwargs):
    #     logger.info("You're in post.")

    #     # リクエストからフォームを作成
    #     form = RegisterForm(request.POST)
    #     # バリデーション
    #     if not form.


def register(requests):
    return render(requests, 'accounts/register.html', {})

def login(requests):
    return HttpResponse('This is login page')

def logout(requests):
    return HttpResponse('This is logout page')

def profile(requests):
    return HttpResponse('This is profile page')