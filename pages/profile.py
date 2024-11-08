from flet import *
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


def profile(page):
    user = page.session.get("user")
    PERSON_ASSETS_FOLDER = os.getenv("PERSON_ASSETS_FOLDER")
    if not user:
        return error(page,"User not logged in", "Home", "/", "home", "green")
    else:
        nav = navBar(user, page, PERSON_ASSETS_FOLDER)
        psts = [post(p) for p in Posts if p["id"] == 1]
        profile_elements = Column(
            controls=[
                nav,
                share(page, PERSON_ASSETS_FOLDER),
                *psts

            ],
            height=800,  # Set a fixed height for the container
            scroll="auto",  # Enable scrolling
        )

        profile_container = Container(
            content=profile_elements,
            padding=padding.only(bottom=50),
            height=800,
        )

        return profile_container
        

    