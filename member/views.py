from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate

from .forms import LoginForm


def login(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']

			user = authenticate(
				username=username,
				password=password
			)
			if user:
				django_login(request, user)
				return redirect('post:post_list')
			
			login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
	else:
		login_form = LoginForm()
	context = {
		'login_form': login_form,
	}
	return render(request, 'member/login.html', context)

def logout(request):
	django_logout(request)
	return redirect('post:post_list')