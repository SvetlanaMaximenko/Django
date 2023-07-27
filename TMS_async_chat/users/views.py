import datetime
import re
import hashlib
import aiohttp_jinja2
from aiohttp import web

from extra import redirect, login_required
from .models import User


salt = b'5gz'


class LogIn(web.View):

    @aiohttp_jinja2.template("users/login.html")
    async def get(self):
        return {}

    async def post(self):
        data = await self.request.post()
        username = data.get('username', '').lower()
        password = data.get('password', '').lower()
        print(username, password)
        try:
            user = await User.get(username=username, password=password)
            print(username, password)
        except Exception as error:
            print(error)
            redirect(self.request, "login")
            return

        else:
            self.login(user)
        return web.json_response({"user": user.id})

    def login(self, user: User):

        self.request.session["user_id"] = user.id
        self.request.session["time"] = str(datetime.datetime.now())

        redirect(self.request, "home")


class Register(web.View):

    @aiohttp_jinja2.template("users/register.html")
    async def get(self):
        print(self.request)

    async def check_username(self) -> str:
        """ Get username from post data, and check is correct """
        data = await self.request.post()
        username = data.get('username', '').lower()
        password = data.get('password', '').lower()

        if not re.match(r'^[a-z]\w{0,9}$', username):
            return ""
        return username, password

    def login(self, user: User):
        self.request.session["user_id"] = user.id
        self.request.session["time"] = str(datetime.datetime.now())

        redirect(self.request, "home")

    async def post(self):
        username, password = await self.check_username()
        print('username', username)

        if not username:
            redirect(self.request, "register")

        try:
            await User.get(username=username)
            # Такой пользователь уже есть!
            redirect(self.request, "login")
        except:
            print("Пользователя нет!")

        hash_object = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # print(password, hash_object)
        # hex_dig = hash_object.hexdigest()

        await User.create(username=username, password=hash_object.hex())
        password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        user = await User.get(username=username, password=password)
        self.login(user)


class Logout(web.View):

    @login_required
    async def get(self):
        self.request.session.pop("user_id")
        redirect(self.request, "home")

