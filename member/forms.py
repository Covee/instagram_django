from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


User = get_user_model()

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		class_update_fields = ['username', 'password']
		for field_name in class_update_fields:
			self.fields[field_name].widget.attrs.update({
				'class': 'form-control'
			})

	
class SignupForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		class_update_fields = ['password1', 'password2']
		for field_name in class_update_fields:
			self.fields[field_name].widget.attrs.update({
				'class': 'form-control'
			})

	class Meta:
		model = User
		fields = (
			'username',
			'password1',
			'password2',
		)
		widgets = {
			'username': forms.TextInput(
				attrs={
					'class': 'form-control',
				}
			),
		}


	# username = forms.CharField(
	# 	widget=forms.TextInput(
	# 		attrs={
	# 			'class': 'form-control',
	# 		}
	# 	)
	# )
	# password1 = forms.CharField(
	# 	widget=forms.PasswordInput(
	# 		attrs={
	# 			'class': 'form-control',
	# 		}
	# 	)
	# )
	# password2 = forms.CharField(
	# 	widget=forms.PasswordInput(
	# 		attrs={
	# 			'class': 'form-control',
	# 		}
	# 	)
	# )

	# def clean_username(self):
	# 	username = self.cleaned_data['username']
	# 	if User.objects.filter(username=username).exists():
	# 		raise forms.ValidationError('아이디가 이미 사용중입니다.')
	# 	return username

	# def clean_password2(self):
	# 	password1 = self.cleaned_data['password1']
	# 	password2 = self.cleaned_data['password2']
	# 	if password1 != password2:
	# 		raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
	# 	return password2

	# def signup(self):
	# 	if self.is_valid():
	# 		return User.objects.create_user(
	# 			username=self.cleaned_data['username'],
	# 			password=self.cleaned_data['password2']
	# 		)