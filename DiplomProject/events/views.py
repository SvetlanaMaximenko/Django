from datetime import datetime, timedelta

# import transaction as transaction
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.http import Http404
from user.forms import UserRegForm, UserLoginForm
from user.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models.query import Q, QuerySet

from django.db import transaction
from events.models import Event, Comment
from events.forms import CommentForm


# Create your views here.
class EventList(View):

    def get_queryset(self):
        search = self.request.GET.get("search_str")
        if search:
            qs = Event.objects.all().filter(Q(name__icontains=search))
        else:
            qs = Event.objects.all()
        return qs

    def get(self, request):
        events = self.get_queryset()
        return render(request, "events/home.html", {"events": events})


class EventMyList(View):

    def get(self, request):
        events = Event.objects.filter(users=request.user.id)
        return render(request, "events/my_events.html", {"events": events})


class EventView(View):

    def get(self, request, event_id: int):
        event = Event.objects.get(id=event_id)
        return render(request, "events/view_event.html", {"event": event})


class AddComment(View):

    def post(self, request, event_id: int):

        form = CommentForm(request.POST)
        event = Event.objects.get(id=event_id)
        user = request.user
        if not form.is_valid():
            return render(request, "events/view_event.html", {"event_id": event.id})
        else:
            with transaction.atomic():
                content = form.cleaned_data["content"]
                print(content)
                comment = Comment(content=content, event_id=event.id, user_id=user.id)
                comment.save()
        return redirect(reverse("view", kwargs={"event_id": event_id}))


class EventEdit(View):

    def get(self, request, event_id: int):
        event = Event.objects.get(id=event_id)
        if not event.users.filter(id=self.request.user.id).exists():
            event.users.add(self.request.user.id)
            event.save()
        else:
            print('Вы уже здесь!')
            str = 'вы подписаны на это событие'
            return render(request, "events/edit_event_error.html")
        events = Event.objects.all()
        return render(request, "events/edit_event.html", {"event": event})

    def post(self, request, event_id: int):
        print('!!')
        event = Event.objects.get(id=event_id)

        return render(request, "events/home.html", {"events": events})
