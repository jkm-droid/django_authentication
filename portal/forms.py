from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class ChangePasswordForm(PasswordChangeForm):

	class Meta:
		model = User
		fields = ['old_password', 'password1', 'password2']


class EditProfileForm(UserChangeForm):

	password = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'type':'hidden'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'password']	

	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)

		self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
		self.fields['email'].help_text = '<small>Email must contain an @</small>'

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
		self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only</small>'

		self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'

		self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
		
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Enter password1'
		self.fields['password1'].help_text = '<small><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric</li></ul></small>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password1'
		self.fields['password2'].help_text = '<small>Enter the same password as before, for verification.</small>'