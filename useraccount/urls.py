from django.urls import path
from useraccount.views import user_login, user_logout, SignupView, profile_view, edit_profile_view, visit_profile, PassWordChange, search

app_name = "user"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("registration/", SignupView.as_view(), name="registration"),
    path("profile/<str:username>/", profile_view, name="profile"),
    path("visit-profile/<int:profileid>/", visit_profile, name="visit_profile"),
    path("edit_profile/<str:username>/", edit_profile_view, name="edit_profile"),
    path("password",PassWordChange.as_view(template_name="password_change_form.html"),name="password-change"),
    path("search/", search, name="search"),
]