from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from inbox.models import Message
from inbox.forms import InboxForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


User = get_user_model()


def message_view(request):
    users = User.objects.filter().exclude(id=request.user.id)
    context = {"users": users}
    return render(request, "message.html", context)


def message_to_user(request, username):
    users = User.objects.filter().exclude(id=request.user.id)
    to_user = User.objects.get(username=username)
    messages = Message.objects.filter(
        from_user__in=[request.user, to_user],
        to_user__in=[request.user, to_user],
    ).order_by("created_at")
    form = InboxForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.from_user = request.user
        
        message.to_user = to_user
        message.save()
        return HttpResponseRedirect(reverse("inbox:message_user", args=(username, )))
    context = {"conversations": messages, "form": form, "users": users, "username": username , "to_user": to_user}
    return render(request, "message.html", context)

@login_required
def delete_message(request):
    messageid = request.POST.get("messageid")
    chat = get_object_or_404(Message, id=messageid, from_user=request.user)
    username = chat.to_user.username
    chat.delete()
    messages.add_message(request, messages.INFO, "Your message deleted succesfully.")
    return HttpResponseRedirect(reverse("inbox:message_user", args=(username, )))