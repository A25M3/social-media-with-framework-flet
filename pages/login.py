from flet import *

from components.header import *
from components.textField import *
from components.costumButton import *
from components.costumImage import *
from components.error import *

from models.user import User

from database import *


def login(page):

    db = Database("data.db")

    password_field = textField(icons.PASSWORD, "Password", True)
    username_field = textField(icons.PERSON, "Username")
    error_message = Text(color="red", size=15)

    def login_handeler(username, password):
        if db.login(username, password):

            page.session.set("user", username)
            page.go("/")
        else:
            error_message.value = "Login failed"
            page.update()

    loginBtn = ElevatedButton(
        "Login",
        width=130,
        bgcolor="black",
        color="white",
        icon="login",
        icon_color="red",
        on_click=lambda e: login_handeler(username_field.value, password_field.value)
        )
    
    login_container = Column(
        controls=[
            header('Login'),

            Container(height=20),

            Row(
                controls=[
                    costumeImage("../assets/login.png"),
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    Text("Login to your account 👌", size=18),
                ],
                alignment=MainAxisAlignment.CENTER
            ),

            Container(height=20),

            Row(controls=[error_message], alignment=MainAxisAlignment.CENTER),
            
            Row(
                controls=[
                    username_field,
                ],
                alignment=MainAxisAlignment.CENTER
            ),

            Row(
                controls=[
                    password_field,
                ],
                alignment=MainAxisAlignment.CENTER
            ),

            Container(height=20),

            Row(
                controls=[
                    costumButton("Home", page, "/", "home", "green"),
                    loginBtn,
                    costumButton("Register", page, "/register", "add", "blue"),
                          ],  # Use home_image function from components
                alignment=MainAxisAlignment.CENTER  # Centering the image horizontally
            ),

        ]
    )

    user = page.session.get("user")

    if user :
        return error(page,"User already logged in", "Profile", "/profile", "person", "blue")
    else :
        return login_container