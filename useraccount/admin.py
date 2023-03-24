from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from useraccount.models import Profile, Education, Job
# Register your models here.

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "contact", "address", "birth_date", "avatar", "age", "height", "marital_status", "religion", "mother_tongue", "country", "bio", "hubby", "favourite_foods", "favourite_places")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("college_name", "degree", "percentage")

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("company_name", "department", "salary")