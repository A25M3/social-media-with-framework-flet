from flet import *
from .photoButton import *

from database import *

def share(page, PERSON_ASSETS_FOLDER):
    db = Database("data.db")
    selected_file = [None]

    share_desc = TextField(
                label="Write what you want to ...",
                multiline=True,
                min_lines=1,
                max_lines=2,
                border=InputBorder.UNDERLINE,
                width=300,
                height=50,
                text_style=TextStyle(size=12)
                )
    

    def createNewPost(e):
        db.addPost(share_desc.value, 1, selected_file[0])
        posts = db.getAllPosts()
        print(posts)
    
    share_top = Row(
        controls=[
            Image(
                src=PERSON_ASSETS_FOLDER + "1.jpeg",
                width=32,
                height=32,
                fit=ImageFit.COVER,
                border_radius=16,
            ),
            
            share_desc,
            
            TextButton(
                text="Share",
                style=ButtonStyle(
                    colors.BLACK
                    ),
                on_click=createNewPost
                )
        ],
        alignment=MainAxisAlignment.SPACE_AROUND
    )
    share_bottom = Row(
        controls=[
            photoButton(page, selected_file, "green", "Photo"),
            TextButton(
                text="Tag", 
                icon="tag", 
                icon_color="blue",
                style=ButtonStyle(colors.BLACK)
                ),
            TextButton(
                text="location", 
                icon=icons.LOCATION_CITY, 
                icon_color="red",
                style=ButtonStyle(colors.BLACK)
                ),
            TextButton(
                text="Feelings", 
                icon=icons.FACE_6_SHARP, 
                icon_color="#EDC967",
                style=ButtonStyle(colors.BLACK)
                ),
        ],alignment=MainAxisAlignment.SPACE_BETWEEN
    )
    share_container = Container(
        content=Column(controls=[
            share_top,
            share_bottom,
        ]),
        bgcolor="#3A03C6FB",
        height=120,
        padding=10,
        border_radius=10,
        margin=margin.only(top=20, bottom=20)
    )

    return share_container