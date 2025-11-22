from django import forms
from .models import StudentInfo, EducationalBackground, FamilyBackground, Account, Subjects
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'studid', 'department', 'year', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a Gmail address")
        return email

    def clean_department(self):
        department = self.cleaned_data.get('department')
        allowed_departments = ['BSIT', 'BSPA', 'ABELS', 'DHRS', 'BSA', 'BSAIS', 'BSE', 'BSSW', 'BTVTED']
        if department not in allowed_departments:
            raise forms.ValidationError(
                "Department should be one of: BSIT, BSPA, ABELS, DHRS, BSA, BSAIS, BSE, BSSW, BTVTED"
            )
        return department

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name

    def clean_studid(self):
        studid = self.cleaned_data.get('studid')
        if len(studid) < 3:
            raise forms.ValidationError("Student ID must be at least 3 characters long")
        return studid

class EducationalBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = ['level', 'school', 'address', 'year', 'attainment']

    def clean_level(self):
        level = self.cleaned_data.get('level')
        if len(level) < 3:
            raise forms.ValidationError("Level must be at least 3 characters long")
        return level

    def clean_school(self):
        school = self.cleaned_data.get('school')
        if len(school) < 3:
            raise forms.ValidationError("School name must be at least 3 characters long")
        return school

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 3:
            raise forms.ValidationError("Address must be at least 3 characters long")
        return address

    def clean_attainment(self):
        attainment = self.cleaned_data.get('attainment')
        if len(attainment) < 3:
            raise forms.ValidationError("Attainment must be at least 3 characters long")
        return attainment

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'studid', 'cpno']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a Gmail address")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be at least 3 characters long")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long")
        return password

class FamilyBackgroundForm(forms.ModelForm):
    class Meta:
        model = FamilyBackground
        fields = ['name', 'occupation', 'salary', 'address', 'cpno']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name

    def clean_occupation(self):
        occupation = self.cleaned_data.get('occupation')
        if len(occupation) < 3:
            raise forms.ValidationError("Occupation must be at least 3 characters long")
        return occupation

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 3:
            raise forms.ValidationError("Address must be at least 3 characters long")
        return address

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['code', 'name', 'units', 'schedule', 'inst']

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if len(code) < 3:
            raise forms.ValidationError("Code must be at least 3 characters long")
        return code

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Subject name must be at least 3 characters long")
        return name

    def clean_units(self):
        units = self.cleaned_data.get('units')
        if units <= 0:
            raise forms.ValidationError("Units must be greater than 0")
        return units

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
