from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from useraccount.forms import SignupForm, ProfileForm, PasswordChangingForm
from django.urls import reverse_lazy
from useraccount.models import Profile, Education, Job
from django.contrib.auth.decorators import login_required
from django.db.models import Q


User = get_user_model()


def user_login(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("story:matches"))
        else:
            messages.add_message(request, messages.ERROR, "Invalid Username or Password")
            return HttpResponseRedirect(reverse("user:login"))

    return render(request, "login.html", {"form": form})

class UserLoginView(LoginView):
    template_name = "login.html"

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:login"))


class SignupView(CreateView):
    template_name = "registration.html"
    form_class = SignupForm
    model = User
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        Education.objects.create(user=user)
        Job.objects.create(user=user)
        return super().form_valid(form)


def get_success_url(self):
    messages.add_message(self.request, messages.INFO, "Your Account Registered Succesfully.")
    return str(self.success_url)

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile=Profile.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    job = Job.objects.filter(user=request.user)
    context = {
        'user': user,
        'profile': profile,
        'education': education,
        'job': job
    }
    
    if request.user.is_authenticated and request.user.username==username:
        return render(request, "profile.html", context)
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
@login_required
def visit_profile(request, profileid):
    profile = Profile.objects.get(id=profileid)
    education = Education.objects.all()
    context = {
        "profile": profile,
        "education": education
    }
    return render(request, "visitprofile.html", context)
    

@login_required
def edit_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    education = get_object_or_404(Education, user=request.user)
    job = get_object_or_404(Job, user=request.user)
    if request.user.is_authenticated and request.user.username==username:
        user=request.user
        initial_data = {"first_name": user.first_name, "last_name": user.last_name, "email": user.email, "college_name": education.college_name, "degree": education.degree, "percentage": education.percentage, "company_name": job.company_name, "department": job.department, "salary": job.salary,}
        form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile, initial=initial_data)
        if form.is_valid():
            obj=form.save(commit=False)
            user=request.user
            user.first_name=form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.email = form.cleaned_data.get("email")
            education.college_name = form.cleaned_data.get("college_name")
            education.degree = form.cleaned_data.get("degree")
            education.percentage = form.cleaned_data.get("percentage")
            job.company_name = form.cleaned_data.get("company_name")
            job.department = form.cleaned_data.get("department")
            job.salary = form.cleaned_data.get("salary")
            user.save()
            education.save()
            job.save()
            obj.save()
            form.save()
            messages.add_message(request, messages.INFO, "Your Profile Updated Succesfully.")
            return HttpResponseRedirect(reverse("user:profile", args=(request.user.username, )))
    return render(request, "edit_profile.html", {"form": form})
 
class PassWordChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url=reverse_lazy("user:login")
    def get_success_url(self):
        message = messages.add_message(self.request, messages.INFO, "Your Password Updated Succesfully.")
        message
        return str(self.success_url)
    
def search(request):
    searchdata = request.GET.get("search")
    user=User.objects.filter(Q(first_name__icontains=searchdata) | Q(last_name__icontains=searchdata)).exclude(id=request.user.id)
    context = {
        'user': user,
    }
    return render(request, "search.html", context)
