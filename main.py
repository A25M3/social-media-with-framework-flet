from flet import *
from views import *
from database import *
# main function
def main(page : Page):
    page.title = 'App | Home'
    page.window.width = 500
    page.window.height = 800
    page.bgcolor = "white"
    page.theme_mode = ThemeMode.LIGHT
    page.padding = 0
    page.window.left = 1024
    page.scroll = "auto"

    db = Database("data.db")

    # Add tables to the database (if not already exists)
    db.addTableUser("user")
    db.addTablePost("post")

    def page_change(route):
        p_route = page.route
        page.views.clear()
        page.views.append(
            views_handler(page)[p_route]
        )

        if p_route == "/":
            page.title = "App | Home"
        elif p_route == "/login":
            page.title = "App | Login"
        elif p_route == "/register":
            page.title = "App | Register"
        elif p_route == "/profile":
            page.title = "App | Profile"

        page.update()

    page.on_route_change = page_change
    page.go('/register') 

app(main)