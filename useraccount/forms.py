from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms
from useraccount.models import Profile, Education, Job

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2", )

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta:
        Model = User
        fields = ("old_password", "new_password1", "new_password2", )

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    college_name = forms.CharField()
    degree = forms.CharField()
    percentage = forms.CharField()
    company_name = forms.CharField()
    department = forms.CharField()
    salary = forms.CharField()
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "gender", "email", "contact", "address", "birth_date", "avatar","age", "height", "marital_status", "religion", "mother_tongue", "country", "bio", "hubby", "favourite_foods", "favourite_places")

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ("college_name", "degree", "percentage")

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("company_name", "department", "salary")
