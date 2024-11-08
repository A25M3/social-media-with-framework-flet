from flet import *
from pages.home import *
from pages.login import *
from pages.register import *
from pages.profile import *

def views_handler(page):
    return {
        "/": View(
            route="/",
            controls=[
                home(page)
            ]
        ),
        "/login": View(
            route="/login",
            controls=[
                login(page)
            ]

        ),
        "/register": View(
            route="/register",
            controls=[
                register(page)
            ]
        ),
        "/profile": View(
            route="/profile",
            controls=[
                profile(page)
            ]
        ),
    }