from .forms import UserRegistrationForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):

    template_name = "home.html"

    return render(request, template_name)

def login_user_view(request):

	template_name = "login.html"

	if request.user.is_authenticated:
		messages.error(request, "you are already logged in")
		return redirect('home')

	else:

		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			#authenticate the user details
			user = authenticate(request, username=username, password=password)

			#if user details are correct
			#login the user
			#otherwise redirect the user to login page
			if user is not None:
				login(request, user)
				messages.success(request, 'Logged in successfully')
				return redirect('home')
			else:
				messages.warning(request, 'Error logging in- Please try again..')
				return redirect('login')

		else:
			return render(request, template_name, {})


	return render(request, template_name, {})

def logout_user_view(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, 'You have been logged out successfully')
		return redirect('home')
	else:
		messages.error(request, "You are already logged out...Log in")
		return redirect('login')


def register_user_view(request):

	template_name = "register.html"

	if request.user.is_authenticated:
		messages.error(request, "You are already registered")
		return redirect('home')
	else:

		#check if the form method if POST
		if request.method == 'POST':
			form = UserRegistrationForm(request.POST)
			#validate the form data
			#save the form if the data is clean
			if form.is_valid():
				form.save()

				#check if the username and password are valid
				#authenticate the details
				#login in the user if the data is valid
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(request, username=username, password=password)
				login(request, user)
				#send a success message to the user
				messages.success(request, 'Registered successfully')
				#redirect to the user homepage
				return redirect('home')

		else:
			form = UserRegistrationForm()

	context = {'form':form}
	return render(request, template_name, context)


def edit_profile_view(request):

	template_name = "edit_profile.html"


	if request.user.is_authenticated:
		#check if the form method if POST
		if request.method == 'POST':
			form = EditProfileForm(request.POST, instance=request.user)
			#validate the form data
			#save the form if the data is clean
			if form.is_valid():
				form.save()

				#send a success message to the user
				messages.success(request, 'profile edited successfully')
				#redirect to the user homepage
				return redirect('home')

		else:
			form = EditProfileForm(instance=request.user)
	else:
		messages.error(request, "You must be logged to edit your profile")
		return redirect('login')

	context = {'form':form}
	return render(request, template_name, context)


def change_password_view(request):
	template_name = "change_password.html"

	if request.user.is_authenticated:
		#check if the form method if POST
		if request.method == 'POST':
			form = ChangePasswordForm(data=request.POST, user=request.user)
			#validate the form data
			#save the form if the data is clean
			if form.is_valid():
				form.save()

				update_session_auth_hash(request, form.user)
				#send a success message to the user
				messages.success(request, 'password changed successfully')
				#redirect to the user homepage
				return redirect('home')

		else:
			form = ChangePasswordForm(user=request.user)
	else:
		messages.error(request, "Log in first to change your password or contact admin")
		return redirect('login')

	context = {'form':form}
	return render(request, template_name, context)
