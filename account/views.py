from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user_input = form.cleaned_data
      user = authenticate(username=user_input['username'], password=user_input['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponse('Вы прошли аутентификацию')
        else:
          return HttpResponse('Аккаунт не активирован')
      else:
        return HttpResponse ('Неверный логин или пароль')
  else:
    form = LoginForm()
  return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})