from datetime import datetime
import method_decorator as method_decorator
import serializers as serializers
import status as status
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.db import transaction
from Events.forms import UserRegForm, UserLoginForm
from Events.models import User, Event
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permisiion import IsListUser, IsSuperUser, IsOwnerReadOnly
from .serialilizers import UserSerializer, EventSerializer


# class AuthToken(ObtainAuthToken):
#
#     def get(self, request):
#         return render(request, "registration/login.html", {"form": UserLoginForm()})
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         print(token, created, user.pk)
#         return Response({
#             'token': token,
#             'created': created,
#             'user_id': user.pk,
#         })
#

class Home(generics.GenericAPIView):

    def get(self, request):
        return render(request, "home.html")


class EventsList(generics.ListAPIView):
    queryset = Event.objects.filter(meeting_time__gt=datetime.now())
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


class EventEdit(generics.GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwnerReadOnly]
    lookup_url_kwarg = "event_id"
    lookup_field = "id"

    # def get_queryset(self, request):
    #     return Event.objects.get(id=request.data['id'])

    def post(self, request, event_id: int):
        if request.method == 'POST':
            event = get_object_or_404(Event, id=event_id)
            print(event)
            # user = self.request.user
            print(self.request.user.username, self.request.user.id)

            event.users.add(self.request.user.id)
            print(event.users)
            event.save()

class EventsListMy(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(users__username=self.request.user.username)


@api_view(['POST'])
def register_user(request):
   if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        print(username, password, email)
        if not username or not email or not password:
            return Response({'error': 'Необходимо заполнить все поля.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return Response({'success': 'Пользователь успешно зарегистрирован.'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Ошибка при регистрации пользователя.'}, status=status.HTTP_400_BAD_REQUEST)


class UserReg(View):

    def get(self, request):
        return render(request, "registration/registration.html", {"form": UserRegForm()})

    def post(self, request):
        form = UserRegForm(request.POST)
        if not form.is_valid():
            return render(request, "registration/registration.html", {"form": UserRegForm()})
        else:
            with transaction.atomic():
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user = User(username=username, email=email, password=password)
                user.save()
                return redirect(reverse("home"))


class UserLogout(LogoutView):
    next_page = '/'



