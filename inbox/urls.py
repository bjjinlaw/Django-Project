from django.urls import path
from inbox.views import message_view, message_to_user, delete_message
app_name="inbox"

urlpatterns = [
    path("messages/", message_view, name="messages"),
    path("messages/<str:username>/", message_to_user, name="message_user"),
    path("delete-message/", delete_message, name="delete_message"),
]