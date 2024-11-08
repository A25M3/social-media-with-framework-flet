from flet import *
from components.header import *
from components.costumImage import *
from components.textField import *
from components.costumButton import *
from components.photoButton import *
from database import *

def register(page):
    db = Database("data.db")

    file_selected = [None]

    password_field = textField(icons.PASSWORD, "Password", True)
    username_field = textField(icons.PERSON, "Username")
    email_field = textField(icons.MAIL, "Email")

    def create_user_handeler(username, email, password):
        db.create_user(username, email, password, file_selected[0])
        users = db.getAllUsers()
        print(users)
        page.go("/login")
    

    registerBtn = ElevatedButton(
        "Register",
        width=130,
        bgcolor="black",
        color="white",
        icon="add",
        icon_color="blue",
        on_click=lambda e: create_user_handeler(username_field.value, email_field.value, password_field.value)
        )
    
    register_container = Column(
        controls=[
            header("Register"),

            Container(height=30),

            Row(
                controls=[
                    costumeImage("../assets/register.png")
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    username_field
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    email_field
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    password_field
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    photoButton(page, file_selected, "black", "Profile Picture")
                ],
                alignment=MainAxisAlignment.CENTER
            ),

            Container(height=30),

            Row(
                controls=[
                    costumButton("Home", page, "/", "home", "green"),
                    costumButton("Login", page, "/login", "login", "red"),
                    registerBtn
                    
                          ],
                alignment=MainAxisAlignment.CENTER  # Centering the image horizontally
            ),
        ]
    )

    return register_container