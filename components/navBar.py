from flet import *

def navBar(text, page, PERSON_ASSETS_FOLDER):
    def logout():
        page.session.clear()
        page.go("/login")

    logoutBtn = ElevatedButton(
        "Logout",
        width=120,
        bgcolor="white",
        color="black",
        icon="logout",
        icon_color="red",
        on_click=lambda e: logout()
        )
    
    navbar_left = Row(
        controls=[
             Image(
                src=PERSON_ASSETS_FOLDER + "1.jpeg",
                width=40,
                height=40,
                fit=ImageFit.COVER,
                border_radius=20,
            ),
            Text(text, color="white", size=20, weight="bold"),
        ],
    )
    navbar_center_logo = IconButton(icon=icons.ALIGN_VERTICAL_TOP_ROUNDED,
                                    icon_color="white",
                                    bgcolor="grey",    
                                    on_click=lambda e:page.go("/")
                                    )
    navbar_container = Container(
        content=Row(
            controls=[
                GestureDetector(
                    on_tap=lambda e: page.go("/profile"),
                    content=navbar_left
                ),
                navbar_center_logo,
                logoutBtn,
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        alignment=alignment.center,
        bgcolor="black",
        padding=padding.only(left=15, right=15, top=10, bottom=10),
    )

    return navbar_container