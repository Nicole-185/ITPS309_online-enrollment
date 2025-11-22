from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import StudentInfo, FamilyBackground, Subjects, Account, EducationalBackground
from .forms import StudentInfoForm, EducationalBackgroundForm, RegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user')

@login_required(login_url='login_user')
def dashboard(request):
    students = StudentInfo.objects.all()
    families = FamilyBackground.objects.all()
    education = EducationalBackground.objects.all()
    accounts = Account.objects.all()
    subjects = Subjects.objects.all()

    student_form = StudentInfoForm()
    education_form = EducationalBackgroundForm()

    context = {
        'students': students,
        'families': families,
        'education': education,
        'accounts': accounts,
        'subjects': subjects,
        'student_form': student_form,
        'education_form': education_form,
        'user': request.user
    }
    return render(request, 'accounts/dashboard.html', context)
