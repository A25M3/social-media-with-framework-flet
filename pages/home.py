from flet import *
from components.costumImage import *  # Adjusted relative import
from components.textField import *
from components.costumButton import *
from components.header import *
from components.navBar import *
from components.costumButton import *
from components.error import *
from components.costumButton import *
from components.share import *
from components.post import *
from dummyData import Posts
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def home(page):
    user = page.session.get("user")
    PERSON_ASSETS_FOLDER = os.getenv("PERSON_ASSETS_FOLDER")
    
    # home page if the user not logged in
    home_without_login_container = Column(
        controls=[
            header("Home"),

            Container(height=80),
            
            Row(
                controls=[
                    Text("Welcome ...", color="black", size=20, weight="bold"),
                    ],
                alignment=MainAxisAlignment.CENTER
            ),

            Container(height=10),

            Row(
                controls=[costumeImage("../assets/home_img.png")],  # Use home_image function from components
                alignment=MainAxisAlignment.CENTER  # Centering the image horizontally
            ),

            Container(height=10),

            Row(
                controls=[
                    Text("You are welcome to my application", color="black", size=15),
                    ],
                alignment=MainAxisAlignment.CENTER
            ),

            Container(height=10),

            Row(
                controls=[
                    costumButton("Login", page, "/login", "login", "green"),
                    costumButton("Register", page, "/register", "add", "blue"),
                          ],  # Use home_image function from components
                alignment=MainAxisAlignment.CENTER  # Centering the image horizontally
            ),
        ]
    )

    
    if user:
        #  home page if the user logged in
        nav = navBar(user, page, PERSON_ASSETS_FOLDER)
        psts = [post(p) for p in Posts]
        elements = Column(
            controls=[
                nav,
                share(page, PERSON_ASSETS_FOLDER),
                *psts

            ],
            height=800,  # Set a fixed height for the container
            scroll="auto",  # Enable scrolling
        )

        home_with_login_container = Container(
            content=elements,
            padding=padding.only(bottom=50),
            height=800,
        )

        home_container = home_with_login_container
    else:
        home_container = home_without_login_container

    

    return home_container  # Return the container that holds the centered image