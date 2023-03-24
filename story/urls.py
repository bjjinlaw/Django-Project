from django.urls import path
from story.views import home, dash, matches

app_name = "story"

urlpatterns = [
    path("", home, name="home"),
    path("dash/", dash, name="dash"),
    path("matches/", matches, name="matches"),
]