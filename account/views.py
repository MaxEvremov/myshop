from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


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


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return render(request,
                        'account/edit_done.html')
        else:
          messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


def register(request):
  if request.method == "POST":
    user_form = UserRegistationForm(request.POST)
    if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request,
             'account/register_done.html',
             {'new_user':new_user})
  else:
      user_form = UserRegistationForm()
      return render(request, 'account/register.html', {'user_form':user_form})


